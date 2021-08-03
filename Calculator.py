from Grade_calculator.imports import *

Global_grade_sum = float()
subject_count = int()


def Eng_Grade_Calculation():
    global Global_grade_sum
    global subject_count

    Subject_Name = ""

    Crit_A = ""
    Crit_B = ""
    Crit_C = ""
    Crit_D = ""

    errorA = True
    errorB = True
    errorC = True
    errorD = True

    while Subject_Name == "":
        Subject_Name = input("What is the name of your subject?")

    while errorA:
        try:
            while Crit_A == "":
                Crit_A = input(f"Please enter all of your grades for Criterion A in {Subject_Name}", type="text",
                               placeholder="Separate the numbers with spaces")
            Crit_A_list = Crit_A.split()
            Crit_A_list = list(map(int, Crit_A_list))
            Crit_A_sum = sum(Crit_A_list[0:len(Crit_A_list)])
            Crit_A_final = Crit_A_sum / len(Crit_A_list)
        except ValueError:
            popup("Error :(", put_text("Please only input numerical values (and no decimals)."))
            Crit_A = ""
        else:
            errorA = False
            if Crit_A_final > 8:
                popup("Error :(",
                      [put_text("You have put a number bigger than 8 as one of your grades, remember that your"
                                " grades only go from 0 to 8, and remember to separate your grades with spaces :)"),
                       put_buttons(["Retry?"], onclick=lambda _: close_popup())])
                Crit_A = ""
                errorA = True

    while errorB:
        try:
            while Crit_B == "":
                Crit_B = input(f"Please do the same with your grades for Criterion B in {Subject_Name}", type="text",
                               placeholder="Separate the numbers with spaces")
            Crit_B_list = Crit_B.split()
            Crit_B_list = list(map(int, Crit_B_list))
            Crit_B_sum = sum(Crit_B_list[0:len(Crit_B_list)])
            Crit_B_final = Crit_B_sum / len(Crit_B_list)
        except ValueError:
            popup("Error :(", put_text("Please only input numerical values (and no decimals)."))
            Crit_B = ""
        else:
            errorB = False
            if Crit_B_final > 8:
                popup("Error :(",
                      [put_text("You have put a number bigger than 8 as one of your grades, remember that your"
                                " grades only go from 0 to 8, and remember to separate your grades with spaces :)"),
                       put_buttons(["Retry?"], onclick=lambda _: close_popup())])
                Crit_B = ""
                errorB = True

    while errorC:
        try:
            while Crit_C == "":
                Crit_C = input(f"Now with Criterion C of {Subject_Name}",
                               type="text", placeholder="Separate the numbers with spaces")
            Crit_C_list = Crit_C.split()
            Crit_C_list = list(map(int, Crit_C_list))
            Crit_C_sum = sum(Crit_C_list[0:len(Crit_C_list)])
            Crit_C_final = Crit_C_sum / len(Crit_C_list)
        except ValueError:
            popup("Error :(", put_text("Please only input numerical values (and no decimals)."))
            Crit_C = ""
        else:
            errorC = False
            if Crit_C_final > 8:
                popup("Error :(",
                      [put_text("You have put a number bigger than 8 as one of your grades, remember that your"
                                " grades only go from 0 to 8, and remember to separate your grades with spaces :)"),
                       put_buttons(["Retry?"], onclick=lambda _: close_popup())])
                Crit_C = ""
                errorC = True

    while errorD:
        try:
            while Crit_D == "":
                Crit_D = input(f"And finally, Criterion D of {Subject_Name}",
                               type="text", placeholder="Separate the numbers with spaces")
            Crit_D_list = Crit_D.split()
            Crit_D_list = list(map(int, Crit_D_list))
            Crit_D_sum = sum(Crit_D_list[0:len(Crit_D_list)])
            Crit_D_final = Crit_D_sum / len(Crit_D_list)
        except ValueError:
            popup("Error :(", put_text("Please only input numerical values (and no decimals)."))
            Crit_D = ""
        else:
            errorD = False
            if Crit_D_final > 8:
                popup("Error :(",
                      [put_text("You have put a number bigger than 8 as one of your grades, remember that your"
                                " grades only go from 0 to 8, and remember to separate your grades with spaces :)"),
                       put_buttons(["Retry?"], onclick=lambda _: close_popup())])
                Crit_D = ""
                errorD = True

    All_Grades_sum = Crit_A_final + Crit_B_final + Crit_C_final + Crit_D_final

    subject_count += 1
    if All_Grades_sum == 0:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("0/10")], size="80% 10px 20%")
        Global_grade_sum += 0
    elif 0 < All_Grades_sum <= 5:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("1/10")], size="80% 10px 20%")
        Global_grade_sum += 1
    elif 5 < All_Grades_sum <= 8:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("2/10")], size="80% 10px 20%")
        Global_grade_sum += 2
    elif 8 < All_Grades_sum <= 11:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("3/10")], size="80% 10px 20%")
        Global_grade_sum += 3
    elif 11 < All_Grades_sum <= 14:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("4/10")], size="80% 10px 20%")
        Global_grade_sum += 4
    elif 14 < All_Grades_sum <= 16:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("5/10")], size="80% 10px 20%")
        Global_grade_sum += 5
    elif 16 < All_Grades_sum <= 20:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("6/10")], size="80% 10px 20%")
        Global_grade_sum += 6
    elif 20 < All_Grades_sum <= 24:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("7/10")], size="80% 10px 20%")
        Global_grade_sum += 7
    elif 24 < All_Grades_sum <= 27:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("8/10")], size="80% 10px 20%")
        Global_grade_sum += 8
    elif 27 < All_Grades_sum <= 29:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("9/10")], size="80% 10px 20%")
        Global_grade_sum += 9
    elif 29 < All_Grades_sum <= 32:
        put_row([put_code("Your LOMCE grade in " + Subject_Name + " is"), None, put_code("10/10")], size="80% 10px 20%")
        Global_grade_sum += 10


def Esp_Grade_Calculation():
    global Global_grade_sum
    global subject_count

    Subject_Name = ""

    Crit_A = ""
    Crit_B = ""
    Crit_C = ""
    Crit_D = ""

    errorA = True
    errorB = True
    errorC = True
    errorD = True

    while Subject_Name == "":
        Subject_Name += input("¿Qué asignatura quieres calcular?", type="text")

    while errorA:
        try:
            while Crit_A == "":
                Crit_A = input(f"Por favor inserta todas tus notas del Criterio A de {Subject_Name}", type="text",
                               placeholder="Separa los números con espacios")
            Crit_A_list = Crit_A.split()
            Crit_A_list = list(map(int, Crit_A_list))
            Crit_A_sum = sum(Crit_A_list[0:len(Crit_A_list)])
            Crit_A_final = Crit_A_sum / len(Crit_A_list)
        except ValueError:
            popup("Error :(", put_text("Por favor solo mete valores numéricos (no decímales)."))
            Crit_A = ""
        else:
            errorA = False
            if Crit_A_final > 8:
                popup("Error :(",
                      [put_text("Has metido un número mallor que 8 en una de tus notas, recuerda que tus notas solo"
                                " van de 0 a 8, y recuerda separar las notas con espacios :)"),
                       put_buttons(["Retry?"], onclick=lambda _: close_popup())])
                Crit_A = ""
                errorA = True

    while errorB:
        try:
            while Crit_B == "":
                Crit_B = input(f"Por favor haz lo mismo con las notas del Criterio B de {Subject_Name}", type="text",
                               placeholder="Separa los números con espacios")
            Crit_B_list = Crit_B.split()
            Crit_B_list = list(map(int, Crit_B_list))
            Crit_B_sum = sum(Crit_B_list[0:len(Crit_B_list)])
            Crit_B_final = Crit_B_sum / len(Crit_B_list)
        except ValueError:
            popup("Error :(", put_text("Por favor solo mete valores numéricos (no decímales)."))
            Crit_B = ""
        else:
            errorB = False
            if Crit_B_final > 8:
                popup("Error :(",
                      [put_text("Has metido un número mallor que 8 en una de tus notas, recuerda que tus notas solo"
                                " van de 0 a 8, y recuerda separar las notas con espacios :)"),
                       put_buttons(["Retry?"], onclick=lambda _: close_popup())])
                Crit_B = ""
                errorB = True

    while errorC:
        try:
            while Crit_C == "":
                Crit_C = input(f"Ahora con el Criterio C de {Subject_Name}",
                               type="text", placeholder="Separa los números con espacios")
            Crit_C_list = Crit_C.split()
            Crit_C_list = list(map(int, Crit_C_list))
            Crit_C_sum = sum(Crit_C_list[0:len(Crit_C_list)])
            Crit_C_final = Crit_C_sum / len(Crit_C_list)
        except ValueError:
            popup("Error :(", put_text("Por favor solo mete valores numéricos (no decímales)."))
            Crit_C = ""
        else:
            errorC = False
            if Crit_C_final > 8:
                popup("Error :(",
                      [put_text("Has metido un número mallor que 8 en una de tus notas, recuerda que tus notas solo"
                                " van de 0 a 8, y recuerda separar las notas con espacios :)"),
                       put_buttons(["Retry?"], onclick=lambda _: close_popup())])
                Crit_C = ""
                errorC = True

    while errorD:
        try:
            while Crit_D == "":
                Crit_D = input(f"Y por último las notas del Criterio D de {Subject_Name}",
                               type="text", placeholder="Separa los números con espacios")
            Crit_D_list = Crit_D.split()
            Crit_D_list = list(map(int, Crit_D_list))
            Crit_D_sum = sum(Crit_D_list[0:len(Crit_D_list)])
            Crit_D_final = Crit_D_sum / len(Crit_D_list)
        except ValueError:
            popup("Error :(", put_text("Por favor solo mete valores numéricos (no decímales)."))
            Crit_D = ""
        else:
            errorD = False
            if Crit_D_final > 8:
                popup("Error :(",
                      [put_text("Has metido un número mallor que 8 en una de tus notas, recuerda que tus notas solo"
                                " van de 0 a 8, y recuerda separar las notas con espacios :)"),
                       put_buttons(["Retry?"], onclick=lambda _: close_popup())])
                Crit_D = ""
                errorD = True

    All_Grades_sum = Crit_A_final + Crit_B_final + Crit_C_final + Crit_D_final

    subject_count += 1
    if All_Grades_sum == 0:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("0/10")], size="80% 10px 20%")
        Global_grade_sum += 0
    elif 0 < All_Grades_sum <= 5:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("1/10")], size="80% 10px 20%")
        Global_grade_sum += 1
    elif 5 < All_Grades_sum <= 8:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("2/10")], size="80% 10px 20%")
        Global_grade_sum += 2
    elif 8 < All_Grades_sum <= 11:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("3/10")], size="80% 10px 20%")
        Global_grade_sum += 3
    elif 11 < All_Grades_sum <= 14:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("4/10")], size="80% 10px 20%")
        Global_grade_sum += 4
    elif 14 < All_Grades_sum <= 16:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("5/10")], size="80% 10px 20%")
        Global_grade_sum += 5
    elif 16 < All_Grades_sum <= 20:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("6/10")], size="80% 10px 20%")
        Global_grade_sum += 6
    elif 20 < All_Grades_sum <= 24:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("7/10")], size="80% 10px 20%")
        Global_grade_sum += 7
    elif 24 < All_Grades_sum <= 27:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("8/10")], size="80% 10px 20%")
        Global_grade_sum += 8
    elif 27 < All_Grades_sum <= 29:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("9/10")], size="80% 10px 20%")
        Global_grade_sum += 9
    elif 29 < All_Grades_sum <= 32:
        put_row([put_code("Tu nota LOMCE en " + Subject_Name + " es"), None, put_code("10/10")], size="80% 10px 20%")
        Global_grade_sum += 10
