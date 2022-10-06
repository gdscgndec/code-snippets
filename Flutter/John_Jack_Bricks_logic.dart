void main() {
  int Total_Bricks = 4, john = 0, jack = 0, Bricks_done = 0, selected_no = 0;  

  for (int Loop = 0; Bricks_done < Total_Bricks; Loop++) {
    if ((Loop % 2) == 0) {
      (Bricks_done +selected_no + 1) < Total_Bricks ?
          print("John  ${selected_no}+1 -> ${selected_no + 1}  ->  ${Bricks_done}+${selected_no + 1}  ->  ${Bricks_done += selected_no + 1}") : 
          print("John  ${selected_no}+1 -> ${selected_no + 1}  ->  ${Bricks_done}+${Total_Bricks - Bricks_done}  ->  ${Bricks_done += Total_Bricks - Bricks_done}");
      john += 1;
      selected_no += 1;
      
    } else {
      (Bricks_done + selected_no * 2) < Total_Bricks ? 
          print("Jack  ${selected_no}*2 -> ${selected_no * 2}  ->  ${Bricks_done}+${selected_no * 2}  ->  ${Bricks_done += selected_no * 2}") : 
          print("Jack  ${selected_no}*2 -> ${selected_no * 2}  ->  ${Bricks_done}+${Total_Bricks - Bricks_done}  ->  ${Bricks_done += Total_Bricks - Bricks_done}");
      jack += 1;
    }
  }
  print(john);
  print(jack);
}
