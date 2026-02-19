"""
Test Suite Runner
Runs all test cases from test_suite.json against the chatbot
"""

import json
from pathlib import Path
from services.router import ChatbotRouter
import sys


def load_test_suite():
    """Load test cases from test_suite.json"""
    test_file = Path("test_suite.json")
    
    if not test_file.exists():
        print(f"❌ Error: {test_file} not found!")
        return None
    
    try:
        with open(test_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading test suite: {e}")
        return None


def run_tests():
    """Run all test cases and display results"""
    
    # Load test suite
    test_cases = load_test_suite()
    if not test_cases:
        return
    
    # Initialize chatbot
    try:
        print("🔧 Initializing chatbot...")
        router = ChatbotRouter()
        print("✅ Chatbot initialized\n")
    except Exception as e:
        print(f"❌ Error initializing chatbot: {e}")
        print("💡 Make sure .env file is configured with Azure OpenAI credentials")
        return
    
    # Run tests
    results = {
        "passed": 0,
        "failed": 0,
        "total": len(test_cases)
    }
    
    failed_tests = []
    
    print("=" * 80)
    print("🧪 Running Test Suite")
    print("=" * 80)
    print()
    
    for test in test_cases:
        test_id = test["id"]
        test_type = test["type"]
        question = test["q"]
        expected = test["target"]
        
        print(f"Test #{test_id} [{test_type}]")
        print(f"  Q: {question}")
        
        try:
            # Get chatbot response
            response = router.route_query(question)
            
            # Check if response matches expected (flexible matching)
            passed = False
            
            if test_type == "KB":
                # For KB tests, check if expected text is in response
                passed = expected.lower() in response.lower()
            
            elif test_type == "DB":
                # For DB tests, check if expected pattern is in response
                if "Yes" in expected and "in stock" in expected:
                    # Stock availability test
                    passed = "yes" in response.lower() and "in stock" in response.lower()
                elif expected == "0 / Out of stock":
                    passed = "0" in response or "out of stock" in response.lower()
                elif expected.startswith("£"):
                    # Price test
                    passed = "£" in response and expected.replace("£", "") in response
                else:
                    # Stock count test
                    passed = expected in response
            
            elif test_type == "Fallback":
                # For fallback tests, check for fallback message
                passed = "i'm sorry" in response.lower() and "cannot answer" in response.lower()
            
            if passed:
                print(f"  ✅ PASSED")
                print(f"  A: {response}")
                results["passed"] += 1
            else:
                print(f"  ❌ FAILED")
                print(f"  Expected: {expected}")
                print(f"  Got:      {response}")
                results["failed"] += 1
                failed_tests.append({
                    "id": test_id,
                    "type": test_type,
                    "question": question,
                    "expected": expected,
                    "got": response
                })
        
        except Exception as e:
            print(f"  ❌ ERROR: {e}")
            results["failed"] += 1
            failed_tests.append({
                "id": test_id,
                "type": test_type,
                "question": question,
                "expected": expected,
                "got": f"ERROR: {e}"
            })
        
        print()
    
    # Display summary
    print("=" * 80)
    print("📊 Test Results Summary")
    print("=" * 80)
    print(f"Total Tests:  {results['total']}")
    print(f"✅ Passed:    {results['passed']}")
    print(f"❌ Failed:    {results['failed']}")
    print(f"Success Rate: {(results['passed'] / results['total'] * 100):.1f}%")
    print("=" * 80)
    
    # Display failed tests details
    if failed_tests:
        print()
        print("❌ Failed Tests Details:")
        print("-" * 80)
        for test in failed_tests:
            print(f"\nTest #{test['id']} [{test['type']}]")
            print(f"  Question: {test['question']}")
            print(f"  Expected: {test['expected']}")
            print(f"  Got:      {test['got']}")
        print("-" * 80)
    
    return results["failed"] == 0


if __name__ == "__main__":
    print()
    success = run_tests()
    print()
    
    if success:
        print("🎉 All tests passed!")
        sys.exit(0)
    else:
        print("⚠️  Some tests failed. Please review the results above.")
        sys.exit(1)
