from datetime import date
import sys, inflect



def date_flow(input_str):
    today = date.today()

    try:
        dob = date.fromisoformat(input_str)
        ans = today - dob
        ans_round= round(ans.total_seconds()/60)
        p = inflect.engine()
        ans_final = p.number_to_words(ans_round, andword="")
        return f"{ans_final.capitalize()} minutes"

    except ValueError:
        sys.exit("Invalid date")




def main():
    print(date_flow(input("Date of Birth:")))

if __name__ == "__main__":
    main()
