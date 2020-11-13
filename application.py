from application_factory import create_application

import services

application = create_application()

application.merge(services.application)


def main():
    application.run(debug=True, host='0.0.0.0', port='8080', reloader=True)


if __name__ == "__main__":
    main()
