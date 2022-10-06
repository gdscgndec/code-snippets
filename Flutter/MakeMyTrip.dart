class OneWayTrip {
  String? From_City, To_City, Departure_Date;
  int? no_of_Travellers;

  OneWayTrip(
      {this.From_City,
      this.To_City,
      this.Departure_Date,
      this.no_of_Travellers});

  Map toMap() {
    return {
      'From_City': From_City,
      'To_City': To_City,
      'Departure': Departure_Date,
      'no_of_Travellers': no_of_Travellers
    };
  }
}

class RoundTrip extends OneWayTrip {
  String? Return_Date;
  RoundTrip(
      {From_City, To_City, Departure_Date, no_of_Travellers, this.Return_Date})
      : super(
            From_City: From_City,
            To_City: To_City,
            Departure_Date: Departure_Date,
            no_of_Travellers: no_of_Travellers);

  // Map toMap() {
  //   return {
  //     'From_City': From_City,
  //     'To_City': To_City,
  //     'Departure_Date': Departure_Date,
  //     'Return_Date': Return_Date,
  //     'no_of_Travellers': no_of_Travellers
  //   };
  // }

  @override
  String toString() {
    // TODO: implement toString
    String Parent_Data = "Parent: " + super.toMap().toString();
    String Child_Data = "\nChild: " + {'Return_Date': Return_Date}.toString();
    return Parent_Data + Child_Data;
  }
}

class MultiCityTrip extends OneWayTrip {
  String? From_City2, To_City2, Departure_Date2;
  int? no_of_Travellers2;

  MultiCityTrip(
      {From_City1,
      To_City1,
      Departure_Date1,
      no_of_Travellers1,
      this.From_City2,
      this.To_City2,
      this.Departure_Date2,
      this.no_of_Travellers2})
      : super(
            From_City: From_City1,
            To_City: To_City1,
            Departure_Date: Departure_Date1,
            no_of_Travellers: no_of_Travellers1);

  @override
  String toString() {
    // TODO: implement toString
    String Parent_Data = "Parent: " + super.toMap().toString();
    String Child_Data = "\nChild: " +
        {
          'From_City2': From_City2,
          'To_City2': To_City2,
          'Departure_Date2': Departure_Date2,
          'no_of_Travellers2': no_of_Travellers2
        }.toString();
    return Parent_Data + Child_Data;
  }
}

void main() {
  print("One Way Trip =>\n"+
        OneWayTrip(
          From_City: 'Delhi',
          To_City: 'Bangalore',
          Departure_Date: '28 July,2021',
          no_of_Travellers: 4)
      .toMap().toString());

  print("\n\nRound Trip =>\n"+
        RoundTrip(
          From_City: 'Delhi',
          To_City: 'Bangalore',
          Departure_Date: '28 July,2021',
          no_of_Travellers: 4,
          Return_Date: '29 July,2021')
      .toString());

  print("\n\nMulti City Trip =>\n"+
        MultiCityTrip(
          From_City1: 'Delhi',
          To_City1: 'Bangalore',
          Departure_Date1: '28 July,2021',
          no_of_Travellers1: 4,
          From_City2: 'Bangalore',
          To_City2: 'Pune',
          Departure_Date2: '30 July,2021',
          no_of_Travellers2: 2,)
      .toString());
}
