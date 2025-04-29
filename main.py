import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    logging.info("Script started.")

    try:
        x = 10/0  # This will raise ZeroDivisionError #ADDED SECRETS 
    except ZeroDivisionError as e:
        #main
        logging.error(f"Error occurred on main: {e}")
        raise

if __name__ == "__main__":
    main()
