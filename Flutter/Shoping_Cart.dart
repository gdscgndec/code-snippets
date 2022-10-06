// @dart=2.9
void main(){
  var menu = {
    "burger":{"title": "veggie burger","price":100,"ratings":2.3},
    "noodles":{"title": "veggie noodles","price":200,"ratings":4.5},
    "maggie":{"title": "veggie maggie","price":250,"ratings":3.5},
  };

  List menu_catagories = menu.keys.toList();
  List menu_values = menu.values.toList();
  
  printmydata(){
    for(int i=0; i<menu_catagories.length;i++){
      print("${menu_catagories[i]} => ");
      for(int j=0;j<menu_values.length;j++){
        print("\t${menu_values[i].keys.toList()[j]} : ${menu_values[i].values.toList()[j]}");
      }
    }
  }

  for(int i=0;i<menu.length;i++){
    for(int j=0;j<menu.length-1;j++){
      if (menu_values[j]["ratings"] > menu_values[j+1]["ratings"]){
        var temp = menu_values[j];
        menu_values[j] = menu_values[j+1];
        menu_values[j+1] = temp;
        
        var temp2 = menu_catagories[j];
        menu_catagories[j] = menu_catagories[j+1];
        menu_catagories[j+1] = temp2;
      }
    }
  }

  // Printing Data after Sorting according to Ratings
  print("\n"+"="*6+"Printing Data after Sorting according to Ratings"+"="*6+"\n");
  printmydata();

  // Promo Codes
  var Promocode1 = 'FLAT20';
  var Promocode2 = 'FLAT40';
  var Selected_promo = Promocode1;
  
  var Dp = menu_values.map((e) => e["price"] -= Selected_promo==Promocode1 ? 20 : 40);
  List Discounted_prices = Dp.toList();
  for(int l=0; l<3;l++){menu_values[l]['price'] = Discounted_prices[l];}
  

  // deleting old values in predefined map
  menu.clear();
  // inserting values in map after sorting and discounting prices
  for(int i=0;i<menu_catagories.length;i++){
    menu[menu_catagories[i]] = menu_values[i];
  }


  // Printing Data after applying Discounts
  print("\n"+"="*11+"Printing Data after applying Discounts"+"="*11+"\n");
  printmydata();

}
