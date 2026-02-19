"""
Tri-Tier Chatbot (CLI) - Main Entry Point
TechGear UK Console Application
"""

import sys
from services.router import ChatbotRouter


def main():
    """Main entry point for the Tri-Tier Chatbot CLI"""
    print("=" * 60)
    print("Welcome to TechGear UK Chatbot")
    print("=" * 60)
    print("Type 'exit' to quit\n")
    
    # Initialize the chatbot router
    try:
        router = ChatbotRouter()
    except Exception as e:
        print(f"Error initializing chatbot: {e}")
        sys.exit(1)
    
    # Main conversation loop
    while True:
        try:
            # Get user input
            user_input = input("User: ").strip()
            
            # Check for exit command
            if user_input.lower() == 'exit':
                print("\nThank you for using TechGear UK Chatbot. Goodbye!")
                break
            
            # Skip empty inputs
            if not user_input:
                continue
            
            # Route the query and get response
            response = router.route_query(user_input)
            
            # Display bot response
            print(f"Bot: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nThank you for using TechGear UK Chatbot. Goodbye!")
            break
        except Exception as e:
            print(f"Bot: An error occurred: {e}\n")


if __name__ == "__main__":
    main()
