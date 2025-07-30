#!/usr/bin/env python3
"""
Smart Task Summarizer + Tagger
Run Script

This script helps you start the application easily with proper environment checks.
"""

import os
import sys
from pathlib import Path

def check_environment():
    """Check if all required environment variables and files exist"""
    
    # Check if .env file exists
    if not Path('.env').exists():
        print("❌ .env file not found!")
        print("📝 Please copy env.example to .env and add your OpenAI API key:")
        print("   copy env.example .env")
        print("   Then edit .env and add: OPENAI_API_KEY=your_key_here")
        print("   Get your API key from: https://platform.openai.com/api-keys")
        return False
    
    # Check if OpenAI API key is set
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("❌ OpenAI API key not configured!")
        print("📝 Please edit .env and add your actual OpenAI API key:")
        print("   OPENAI_API_KEY=your_actual_key_here")
        print("   Get your API key from: https://platform.openai.com/api-keys")
        return False
    
    print("✅ Environment configuration looks good!")
    return True

def install_dependencies():
    """Check and install required dependencies"""
    try:
        import flask
        import openai
        print("✅ All dependencies are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("📦 Installing required packages...")
        os.system(f"{sys.executable} -m pip install -r requirements.txt")
        return True

def main():
    """Main entry point"""
    print("🎯 Smart Task Summarizer + Tagger")
    print("=" * 50)
    
    # Check environment
    if not check_environment():
        return
    
    # Check dependencies
    if not install_dependencies():
        return
    
    print("\n🚀 Starting the application...")
    print("📡 The app will be available at: http://localhost:5000")
    print("📖 Check README.md for usage instructions")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Import and run the Flask app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n\n👋 Application stopped. Thank you for using Smart Task Summarizer!")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        print("📖 Check README.md for troubleshooting steps")

if __name__ == "__main__":
    main() 