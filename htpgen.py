import argparse


def main():
    parser = argparse.ArgumentParser(prog="htpgen",
                                     description="Simple lightweight .htpasswd line generator, no Apache required")
    parser.add_argument("user", help="the name of the user")
    parser.add_argument("password", help="the password to use")

    args = parser.parse_args()

    return


if __name__ == "__main__":
    main()
