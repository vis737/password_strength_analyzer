import sys

def analyze_password(password: str) -> dict:
    """
    Evaluates password strength using a single-pass character scan across 5 criteria:
    1. Minimum length (>= 8 characters)
    2. Uppercase letter check
    3. Lowercase letter check
    4. Digit check
    5. Special character / symbol check
    
    Returns a structured report containing individual check results, score (0-5),
    strength label ('Weak', 'Medium', 'Strong'), and targeted feedback for failed checks.
    """
    if password is None:
        password = ""

    # Step 1: Input kept as-is (original string un-mutated)
    
    # Step 2: Check length (min 8)
    has_length = len(password) >= 8

    # Step 3: Scan for character types — single pass, 4 flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    # Step 4: Tally a score (0 - 5)
    checks = {
        "length": has_length,
        "uppercase": has_upper,
        "lowercase": has_lower,
        "digit": has_digit,
        "special": has_special,
    }
    
    score = sum(1 for passed in checks.values() if passed)

    # Step 5: Map score to strength label
    # 0-2 -> Weak, 3-4 -> Medium, 5 -> Strong
    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    else:
        label = "Strong"

    # Step 6: Targeted feedback for failed checks
    feedback = []
    if not has_length:
        feedback.append(f"Increase password length to at least 8 characters (current: {len(password)}).")
    if not has_upper:
        feedback.append("Include at least one uppercase letter (A-Z).")
    if not has_lower:
        feedback.append("Include at least one lowercase letter (a-z).")
    if not has_digit:
        feedback.append("Include at least one numeric digit (0-9).")
    if not has_special:
        feedback.append("Include at least one special character or symbol (e.g., !@#$%^&*).")

    # Step 7 & 8: Return comprehensive report
    return {
        "password_length": len(password),
        "score": score,
        "max_score": 5,
        "label": label,
        "checks": checks,
        "feedback": feedback
    }


def print_report(report: dict) -> None:
    """Pretty prints the password evaluation report to stdout."""
    print("\n==========================================")
    print("      SENTINEL PASSWORD STRENGTH REPORT    ")
    print("==========================================")
    print(f"Password Length : {report['password_length']} characters")
    print(f"Overall Score   : {report['score']} / {report['max_score']}")
    print(f"Strength Label  : {report['label'].upper()}")
    print("------------------------------------------")
    print("Validation Matrix:")
    labels = {
        "length": "Length >= 8 characters",
        "uppercase": "Uppercase Letter (A-Z)",
        "lowercase": "Lowercase Letter (a-z)",
        "digit": "Numeric Digit (0-9)",
        "special": "Special Character / Symbol"
    }
    for key, passed in report["checks"].items():
        status = "[PASS]" if passed else "[FAIL]"
        print(f"  {status} {labels[key]}")
    
    print("------------------------------------------")
    if report["feedback"]:
        print("Targeted Actionable Feedback:")
        for item in report["feedback"]:
            print(f"  - {item}")
    else:
        print("All criteria met! Excellent password security.")
    print("==========================================\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        pwd = sys.argv[1]
    else:
        try:
            pwd = input("Enter password to evaluate: ")
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)
    
    report = analyze_password(pwd)
    print_report(report)
