"""
RPC Interactive Client - Remote Procedure Call Demo (XML-RPC)
=============================================================
This interactive client allows users to call remote methods with custom parameters.

Features:
- Interactive menu for calling different remote methods
- User can input custom names for the greet() method
- Error handling and user-friendly feedback
- Multiple calls in one session

Usage:
1. Start the RPC server: python server.py
2. Run this client: python client_interactive.py
3. Follow the interactive prompts
"""

import xmlrpc.client
import sys

# Server endpoint URL
HOST = 'http://127.0.0.1:9001'

print("=" * 70)
print("RPC INTERACTIVE CLIENT - Remote Procedure Call Demo")
print("=" * 70)
print(f"Server: {HOST}")
print("=" * 70)

try:
    # Create proxy to remote server
    print(f"\n[CLIENT] Connecting to RPC Server at {HOST}...")
    proxy = xmlrpc.client.ServerProxy(HOST)
    print("[CLIENT] ✓ Connected successfully!")
    
    # Test connection by calling a method
    print("[CLIENT] Testing connection...")
    test_response = proxy.greet("Test")
    print("[CLIENT] ✓ Connection verified!")
    
    print("\n" + "=" * 70)
    print("You can now call remote methods on the server.")
    print("Available methods:")
    print("  1. greet(name)           : Get a personalized greeting")
    print("  2. add(a, b)             : Add two numbers")
    print("  3. multiply(a, b)        : Multiply two numbers")
    print("  4. get_server_info()     : Get server information")
    print("  5. echo(message)         : Echo a message")
    print("=" * 70)
    
    call_count = 0
    
    while True:
        print("\n" + "-" * 70)
        print("Choose a remote method to call:")
        print("  1. greet(name)")
        print("  2. add(a, b)")
        print("  3. multiply(a, b)")
        print("  4. get_server_info()")
        print("  5. echo(message)")
        print("  6. Exit")
        print("-" * 70)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            # Call greet method
            name = input("\nEnter a name to greet: ").strip()
            if not name:
                print("[WARNING] Name cannot be empty.")
                continue
            
            try:
                print(f"\n[RPC CALL] Invoking: greet('{name}')")
                response = proxy.greet(name)
                call_count += 1
                print(f"[RESPONSE] {response}")
                print(f"[SUCCESS] Remote call #{call_count} completed!")
            except Exception as e:
                print(f"[ERROR] {e}")
        
        elif choice == '2':
            # Call add method
            try:
                a = float(input("\nEnter first number: "))
                b = float(input("Enter second number: "))
                
                print(f"\n[RPC CALL] Invoking: add({a}, {b})")
                response = proxy.add(a, b)
                call_count += 1
                print(f"[RESPONSE] Result: {response}")
                print(f"[SUCCESS] Remote call #{call_count} completed!")
            except ValueError:
                print("[ERROR] Invalid number format.")
            except Exception as e:
                print(f"[ERROR] {e}")
        
        elif choice == '3':
            # Call multiply method
            try:
                a = float(input("\nEnter first number: "))
                b = float(input("Enter second number: "))
                
                print(f"\n[RPC CALL] Invoking: multiply({a}, {b})")
                response = proxy.multiply(a, b)
                call_count += 1
                print(f"[RESPONSE] Result: {response}")
                print(f"[SUCCESS] Remote call #{call_count} completed!")
            except ValueError:
                print("[ERROR] Invalid number format.")
            except Exception as e:
                print(f"[ERROR] {e}")
        
        elif choice == '4':
            # Call get_server_info method
            try:
                print(f"\n[RPC CALL] Invoking: get_server_info()")
                response = proxy.get_server_info()
                call_count += 1
                print(f"[RESPONSE] Server Information:")
                for key, value in response.items():
                    print(f"  - {key}: {value}")
                print(f"[SUCCESS] Remote call #{call_count} completed!")
            except Exception as e:
                print(f"[ERROR] {e}")
        
        elif choice == '5':
            # Call echo method
            message = input("\nEnter a message to echo: ").strip()
            if not message:
                print("[WARNING] Message cannot be empty.")
                continue
            
            try:
                print(f"\n[RPC CALL] Invoking: echo('{message}')")
                response = proxy.echo(message)
                call_count += 1
                print(f"[RESPONSE] {response}")
                print(f"[SUCCESS] Remote call #{call_count} completed!")
            except Exception as e:
                print(f"[ERROR] {e}")
        
        elif choice == '6':
            print("\n[CLIENT] Exiting...")
            break
        
        else:
            print("[WARNING] Invalid choice. Please enter 1-6.")
    
    print("\n" + "=" * 70)
    print(f"[SUMMARY] Total remote calls made: {call_count}")
    print("[CLIENT] Session ended.")
    print("=" * 70)

except ConnectionRefusedError:
    print("\n[ERROR] ✗ Connection refused!")
    print("Make sure the RPC server is running: python server.py")
    sys.exit(1)
    
except xmlrpc.client.Fault as err:
    print(f"\n[RPC ERROR] Remote method error: {err}")
    sys.exit(1)
    
except KeyboardInterrupt:
    print("\n\n[INFO] Interrupted by user (Ctrl+C)")
    sys.exit(0)
    
except Exception as e:
    print(f"\n[ERROR] An unexpected error occurred: {e}")
    sys.exit(1)
