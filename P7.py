import pandas as pd
import sys

def main(city_name):
    df = pd.read_csv('/home/nineleaps/caps_updated_rooms.csv')
    df['PPN'] = df['PPN'].replace({'₹': '', ',': ''}, regex=True).astype(float)

    city_data = df[df['City'].str.lower() == city_name.lower()]
    if city_data.empty:
        print(f"No data found for the city: {city_name}")
        return

    best_room = city_data.loc[city_data['Reviews'].idxmax()]
    print(f"Best Room Type: {best_room['PType']}")

    cheapest_room = city_data.loc[city_data['PPN'].idxmin()]
    print(f"Cheapest Room: {cheapest_room['PType']}, Location: {cheapest_room['Location ']}, Price: ₹{cheapest_room['PPN']}")

    costliest_room = city_data.loc[city_data['PPN'].idxmax()]
    print(f"Costliest Room: {costliest_room['PType']}, Location: {costliest_room['Location ']}, Price: ₹{costliest_room['PPN']}")

    average_ppn = city_data['PPN'].mean()
    print(f"Average PPN for {city_name}: ₹{average_ppn:.2f}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hotel_info.py <City Name>")
    else:
        main(sys.argv[1])