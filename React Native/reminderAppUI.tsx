import React from 'react'
import { Platform, StatusBar, StyleSheet, Text, View } from 'react-native';
import { List, Colors, Card } from 'react-native-paper';

// Icons from react native paper
// https://materialdesignicons.com/

export default function Reminder() {

    const myList = ["Reminder", "Family"];
    const colorsList = [Colors.yellow800, Colors.yellow600];

    const number = 8;

    function card() {
      return myList.map((element, index) => {
        return (
        <View key={index} style={{flexDirection: 'column'}}>
          <View style={styles.listItem}>
            <View style={styles.listItemLeft}>
              <View style={[styles.circle, {backgroundColor: colorsList[index]}]}>
                <List.Icon color={Colors.white} icon="menu" style={styles.icon}></List.Icon>
              </View>
              <Text style={styles.listText}>{element}</Text>
            </View>
            <View style={styles.listItemLeft}>
              <Text style={[styles.listText, {color: Colors.grey500}]}>{number}</Text>
              <List.Icon icon="chevron-right" color={Colors.grey700}></List.Icon>
            </View>
          </View>
          <View style={styles.divider}></View>
        </View>
        )
      })
    }

    return (
      <View style={styles.container}>
        
        <Text style={styles.editText}>Edit</Text>

        <View style={styles.cardContainer}>
          <View style={styles.card}>
            <View>
              <View style={[styles.circle, {backgroundColor: Colors.blue500}]}><List.Icon color={Colors.white} icon="calendar" style={styles.icon} /></View>
              <Text style={styles.cardText}>Today</Text>
            </View>
            <Text style={styles.text}>{number}</Text>
          </View>

          <View style={styles.card}>
            <View>
              <View style={[styles.circle, {backgroundColor: Colors.red400}]}><List.Icon color={Colors.white} icon="keyboard" style={styles.icon} /></View>
              <Text style={styles.cardText}>Scheduled</Text>
            </View>
            <Text style={styles.text}>{number}</Text>
          </View>
        </View>

        <View style={styles.cardContainer}>
          <View style={styles.card}>
            <View>
              <View style={[styles.circle, {backgroundColor: Colors.blueGrey500}]}><List.Icon color={Colors.white} icon="purse" style={styles.icon} /></View>
              <Text style={styles.cardText}>All</Text>
            </View>
            <Text style={styles.text}>{number}</Text>
          </View>

          <View style={styles.card}>
            <View>
              <View style={[styles.circle, {backgroundColor: Colors.yellow800}]}><List.Icon color={Colors.white} icon="flag" style={styles.icon} /></View>
              <Text style={styles.cardText}>Flagged</Text>
            </View>
            <Text style={styles.text}>{number}</Text>
          </View>
        </View>

        <Text style={styles.text}>My Lists</Text>
        <View style={styles.listContainer}>{card()}</View>

      </View>
    )
  }
  
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: 'black',
      padding: 20,
    },

    editText: {
      fontSize: 17,
      color: Colors.blue500, 
      textAlign: "right", 
      marginTop: 10,
      marginBottom: 15,
    },

    cardContainer: {
      width: Platform.OS === "android" ? "100%": "50%",
      alignSelf: "center",
      flexDirection: 'row',
      justifyContent: "center"
    },

    card: {
      width: Platform.OS === "android" ? "48%": "100%",
      // height: 85,
      flexDirection: 'row',
      backgroundColor: Colors.grey900,
      margin: 8,
      padding: 10,
      borderRadius: 10,
      justifyContent: "space-between",
    },

    icon: {
      alignSelf: "center",
      top: -12,
    },
    
    cardText: {
      fontSize: 16,
      color: Colors.grey500,
      marginTop: 12
    },

    text: {
      color: Colors.white,
      fontSize: 25,
      fontWeight: 'bold',
      marginRight: 10,
      marginLeft: 20,
    },
    
    circle: {
      height:32, 
      width:32, 
      borderRadius:15,
    },

    listContainer: {
      width: "100%",
      // height: 100,
      backgroundColor: Colors.grey900,
      flexDirection: "column",
      margin: 10,
      borderRadius: 15,
      alignSelf: "center"
    }, 

    listItem: {
      alignItems: "center",
      flexDirection: "row",
      paddingLeft: 10,
      justifyContent: "space-between",
    },

    listText: {
      fontSize: 18,
      color: Colors.grey300,
      marginLeft: 20,
    },

    listItemLeft: {
      alignItems: "center",
      flexDirection: "row",
    },

    divider: {
      height: 1,
      width: "80%",
      backgroundColor: Colors.grey800,
      alignSelf: "flex-end",
      marginRight: 15,
      marginBottom: 2,
    }
  });
