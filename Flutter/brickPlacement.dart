import 'package:flutter/material.dart';

class BricksPage extends StatefulWidget {
  const BricksPage({Key? key}) : super(key: key);

  @override
  _BricksPageState createState() => _BricksPageState();
}

class _BricksPageState extends State<BricksPage> {

  TextEditingController noOfBricks = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.deepPurple[100],
      appBar: AppBar(
        backgroundColor: Colors.deepPurple,
        title: Text("Another Brick In the Wall", style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold, fontFamily: 'cursive', color: Colors.deepPurple[100]),),
        centerTitle: true,
      ),
      body : Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            // margin: EdgeInsets.only(top: 100),
            padding: EdgeInsets.only(left: 25, right: 25),
            child: Column(
              children: [
                TextFormField(
                  controller: noOfBricks,
                  decoration: InputDecoration(
                      labelStyle: TextStyle(
                        color: Colors.deepPurple,
                        fontSize: 20,
                      ),
                      labelText: "Number of Bricks",
                      enabledBorder: OutlineInputBorder(
                        borderSide: BorderSide(
                          color: Colors.deepPurple,
                        ),
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderSide: BorderSide(
                          color: Colors.deepPurple,
                        ),
                      )
                  ),
                ),
                SizedBox(height: 20,),
                OutlinedButton(
                    onPressed: (){
                      Navigator.push(context, MaterialPageRoute(builder: (context) => ConclusionPage(bricksNumber: int.parse(noOfBricks.text),)));
                    },
                    child: Text("Conclusion", style: TextStyle(color: Colors.deepPurple),),
                ),
              ],
            )
          ),
        ],
      ),
    );
  }
}

class ConclusionPage extends StatelessWidget {
  int? bricksNumber;
  ConclusionPage({Key? key, this.bricksNumber}) : super(key: key);

  johnJackBricksPlacement(){
    var bricks = bricksNumber, turn = 0, johnCount = 0, jackCount = 0, john = 0, jack = 0, bricksApplied = 0, bricksLeft = bricks! - bricksApplied;
    var list = <Widget>[];
    while ((bricksLeft) > 0) {
      john++;
      jack = john * 2;
      if (bricksLeft <= john && turn == 0) {
        john = bricksLeft;
        bricksApplied += john;
        johnCount++;
        list.add(ListTile(title: Text("John's Turn"), subtitle: Text("Number of Bricks Placed: $john"), tileColor: Colors.deepPurple[200],));
        break;
      } else if (turn == 0) {
        bricksApplied += john;
        johnCount++;
        turn = 1;
      }
      bricksLeft = bricks - bricksApplied;
      list.add(ListTile(title: Text("John's Turn"), subtitle: Text("Number of Bricks Placed: $john"), tileColor: Colors.deepPurple[200],));

      if (bricksLeft <= jack && turn == 1) {
        jack = bricksLeft;
        bricksApplied += jack;
        jackCount++;
        list.add(ListTile(title: Text("Jack's Turn"), subtitle: Text("Number of Bricks Placed: $jack"),));
        break;
      } else if (turn == 1) {
        bricksApplied += jack;
        jackCount++;
        turn = 0;
      }
      bricksLeft = bricks - bricksApplied;

        list.add(ListTile(title: Text("Jack's Turn"), subtitle: Text("Number of Bricks Placed: $jack"),));

    }
    return list + [
      SizedBox(height: 20,),
      Text("Conclusions", style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),),
      SizedBox(height: 10,),
      ListTile(title: Text("How many Turns of John ?"), subtitle: Text("$johnCount"), tileColor: Colors.deepPurple[50],),
      ListTile(title: Text("How many Turns of Jack ?"), subtitle: Text("$jackCount"),),
      turn==0 ? Column(children: [
        ListTile(title: Text("Who placed the last brick ?"), subtitle: Text("John"), tileColor: Colors.deepPurple[50],),
        ListTile(title: Text("How many bricks were placed lastly"), subtitle: Text("$john"),),
      ],) : Column(children: [
        ListTile(title: Text("Who placed the last brick ?"), subtitle: Text("Jack"), tileColor: Colors.deepPurple[50],),
        ListTile(title: Text("How many bricks were placed lastly ?"), subtitle: Text("$jack"),),
      ],),
    ];

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.deepPurple[100],
      appBar: AppBar(
        backgroundColor: Colors.deepPurple,
        title: Text("Another Brick In the Wall", style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold, fontFamily: 'cursive', color: Colors.deepPurple[100]),),
      ),
      body: ListView(
        children: [
          Column(
            children: [
              SizedBox(height: 20,),
              Text("Bricks Placed by John and Jack", style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),),
              SizedBox(height: 5,),
              ListTile(
                title: Column(
                  children: johnJackBricksPlacement(),
                ),
              ),
            ],
          )
        ]
      ),
    );
  }
}
