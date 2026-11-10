
import argparse
import smtplib
from email.message import EmailMessage


def main():
    parser = argparse.ArgumentParser(
        description="Send an email through a remote SMTP server."
    )

    parser.add_argument(
        "ip",
        help="Receiving computer's Tailscale IP address"
    )

    parser.add_argument(
        "message",
        help="Message text; wrap it in quotes"
    )

    parser.add_argument("--port", type=int, default=1025)

    parser.add_argument(
        "--subject",
        default="SMTP Test - Unit 03"
    )

    parser.add_argument(
        "--from",
        dest="sender",
        default="catalin@example.com"
    )

    parser.add_argument(
        "--to",
        dest="recipient",
        default="flavius@example.com"
    )

    args = parser.parse_args()

    email = EmailMessage()

    email["From"] = args.sender
    email["To"] = args.recipient
    email["Subject"] = args.subject

    email.set_content(
        args.message,
        cte="quoted-printable"
    )

    try:
        with smtplib.SMTP(
            args.ip,
            args.port,
            timeout=10
        ) as server:

            server.send_message(email)

    except (OSError, smtplib.SMTPException) as error:
        print(f"Error sending email: {error}")
        return 1

    print("Email accepted by the receiving server!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
