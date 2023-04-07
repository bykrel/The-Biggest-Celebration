while True:

   inputn = input("\nIf you want to be informed about the biggest holiday, October 29, press [N], if you want to exit, press [Q]: ")

   if inputn=="N":
      print("""
      Who is Ataturk? [O]
      Contributions of the Republic to Turkey [L]
      When is the Republic Day of Turkey? [K]
      """)
      
   elif inputn=="Q":
      print("""'EN BÜYÜK BAYRAMDIR!'
                  -Mustafa Kemal Atatürk

            Happy Republic Day, October 29th """)
      break

   inputtask = input("\nPress the button assigned to the information you want to learn: ")

   if inputtask=="O":
      print("Atatürk came to prominence for his role in securing the Ottoman Turkish victory at the Battle of Gallipoli (1915) \nduring World War I. Following the defeat and dissolution of the Ottoman Empire, \nhe led the Turkish National Movement, which resisted mainland Turkey's partition among the victorious Allied powers.")

   elif inputtask=="L":
      print("""1. Madrassas were closed,new and modern schools were opened.
               2. The Arabic letters were removed.With the letter revolution, the Turkish alphabet (abece) was adopted.
               3. Innovations were also made in the clothing belt.
               4. The units of measurement have been changed.
               5. The surname law was enacted.Mustafa Kemale Atatürk was given the surname
               6. Our women have been given the right to choose and be elected.
               7. Equality of men and women has been achieved
               8. The affairs of religion and state were separated.This is called secularism.
               9. Courts operating according to the rules of religion were abolished.
               10. New tools began to be used in agriculture.Electricity and telephone were taken to the villages.
               11. Roads, bridges, dams, ports, factories, airports, railways were built all over our country.
               """)

   elif inputtask=="K":
      print("Saturday October 29, 2022 is the Republic Day of Turkey.")