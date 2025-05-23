# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K94oyVseCSVsbQhiGxYBUbUyrG5nTKy0
"""

import re

def check_password_strength(password):
    """Check if the password meets strength requirements."""
    if len(password) < 8:
        return "❌ Your password must have at least 8 characters."
    if not re.search(r"[A-Z]", password):
        return "❌ Your password must have at least 1 uppercase letter."
    if not re.search(r"[a-z]", password):
        return "❌ Your password must have at least 1 lowercase letter."
    if not re.search(r"[0-9]", password):
        return "❌ Your password must have at least 1 number."
    if not re.search(r"[!@#$%^&*()_+=\-{}\[\]|\\:;'<>,.?/~`]", password):
        return "❌ Your password must have at least 1 special character (!@#$%^ etc.)."
    return "✅ Strong password!"

def main():
    print("=== Create Your Secure Password ===")
    print("Rules:")
    print("- At least 8 characters")
    print("- Include uppercase & lowercase letters")
    print("- Include numbers")
    print("- Include special characters (!@#$%^ etc.)")

    while True:
        password = input("\nEnter your password: ")
        feedback = check_password_strength(password)

        if feedback.startswith("✅"):
            print(feedback)
            print("\n🎉 Password created successfully!")
            break
        else:
            print(feedback)
            print("Please try again.")

if __name__ == "__main__":
    main()