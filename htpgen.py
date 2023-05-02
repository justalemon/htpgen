#!/usr/bin/env python3

import argparse

import bcrypt


def main():
    parser = argparse.ArgumentParser(prog="htpgen",
                                     description="Simple lightweight .htpasswd line generator, no Apache required")
    parser.add_argument("username", help="the name of the user")
    parser.add_argument("password", help="the password to use")

    args = parser.parse_args()

    username = args.username
    password = args.password.encode("utf-8")
    salt = bcrypt.gensalt(rounds=10)
    generated = bcrypt.hashpw(password, salt).decode("utf-8")

    print(f"{username}:{generated}")


if __name__ == "__main__":
    main()
