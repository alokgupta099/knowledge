# ==========================================
#        KRISHI SATHI AI
# Fertilizer & Pesticide Calculator
# Multi Language Support
# ==========================================


print("====================================")
print("          KRISHI SATHI AI")
print("====================================")

print("""
Select Language / भाषा छान्नुहोस्:

1. English
2. नेपाली
3. हिन्दी
4. मैथिली
""")

language = int(input("Enter your choice: "))


# Common Farm Data
crop = "Rice"
soil = "Loamy"
area = 2.5   # hectare


# Variables
fertilizer = ""
fertilizer_amount = 0

organic_pesticide = ""
organic_amount = 0

chemical_pesticide = ""
chemical_amount = 0



# Calculation

if crop == "Rice":

    fertilizer = "Urea + DAP + Potash"
    fertilizer_amount = area * 120

    organic_pesticide = "Neem Oil + Garlic Extract"
    organic_amount = area * 5

    chemical_pesticide = "Chlorantraniliprole"
    chemical_amount = area * 0.5


elif crop == "Wheat":

    fertilizer = "Urea + DAP"
    fertilizer_amount = area * 100

    organic_pesticide = "Neem Oil"
    organic_amount = area * 4

    chemical_pesticide = "Imidacloprid"
    chemical_amount = area * 0.4


elif crop == "Maize":

    fertilizer = "Urea + DAP + Potash"
    fertilizer_amount = area * 110

    organic_pesticide = "Neem Oil + Turmeric Extract"
    organic_amount = area * 5

    chemical_pesticide = "Lambda Cyhalothrin"
    chemical_amount = area * 0.5



# Language Output

print("\n====================================")


if language == 1:
    print("        KRISHI SATHI AI RESULT")
    print("====================================")

    print("Crop Type :", crop)
    print("Soil Type :", soil)
    print("Area :", area, "hectare")

    print("\nRecommended Fertilizer:")
    print(fertilizer)
    print("Quantity:", fertilizer_amount, "kg")

    print("\nOrganic Pesticide:")
    print(organic_pesticide)
    print("Quantity:", organic_amount, "litre")

    print("\nArtificial Pesticide:")
    print(chemical_pesticide)
    print("Quantity:", chemical_amount, "litre")



elif language == 2:
    print("        कृषि साथी AI परिणाम")
    print("====================================")

    print("बाली:", "धान")
    print("माटोको प्रकार:", "दोमट")
    print("क्षेत्रफल:", area, "हेक्टर")

    print("\nसिफारिस गरिएको मल:")
    print("युरिया + डीएपी + पोटास")
    print("मात्रा:", fertilizer_amount, "केजी")

    print("\nजैविक विषादी:")
    print("नीमको तेल + लसुनको झोल")
    print("मात्रा:", organic_amount, "लिटर")

    print("\nरासायनिक विषादी:")
    print("Chlorantraniliprole")
    print("मात्रा:", chemical_amount, "लिटर")



elif language == 3:
    print("        कृषि साथी AI परिणाम")
    print("====================================")

    print("फसल:", "धान")
    print("मिट्टी का प्रकार:", "दोमट")
    print("क्षेत्र:", area, "हेक्टेयर")

    print("\nअनुशंसित उर्वरक:")
    print("यूरिया + डीएपी + पोटाश")
    print("मात्रा:", fertilizer_amount, "किलो")

    print("\nजैविक कीटनाशक:")
    print("नीम तेल + लहसुन अर्क")
    print("मात्रा:", organic_amount, "लीटर")

    print("\nरासायनिक कीटनाशक:")
    print("Chlorantraniliprole")
    print("मात्रा:", chemical_amount, "लीटर")



elif language == 4:
    print("        कृषि साथी AI परिणाम")
    print("====================================")

    print("फसल:", "धान")
    print("माटिक प्रकार:", "दोमट")
    print("जमीन:", area, "हेक्टेयर")

    print("\nअनुशंसित खाद:")
    print("यूरिया + डीएपी + पोटाश")
    print("मात्रा:", fertilizer_amount, "किलो")

    print("\nजैविक कीटनाशक:")
    print("नीमक तेल + लहसुन अर्क")
    print("मात्रा:", organic_amount, "लीटर")

    print("\nरासायनिक कीटनाशक:")
    print("Chlorantraniliprole")
    print("मात्रा:", chemical_amount, "लीटर")



else:
    print("Invalid Language Choice!")



print("\n====================================")
print("Thank You! 🌱")
print("====================================")