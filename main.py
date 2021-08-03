from Grade_calculator import Calculator
from Grade_calculator.Calculator import *
from Grade_calculator.how_does_it_work import *


def main():
    Calculator.subject_count = 0
    clear()

    def Eng_Global_average():
        if Calculator.subject_count > 0:
            global_average = Calculator.Global_grade_sum / Calculator.subject_count
            popup('Global Average', put_text(f"You have an average of {global_average}/10 between all of your grades."))
        else:
            popup("Error :(", put_text('Calculate some grades first!'))

    def Esp_Global_average():
        if Calculator.subject_count > 0:
            global_average = Calculator.Global_grade_sum / Calculator.subject_count
            popup('Media Global', put_text(f"Tienes una media de {global_average}/10 entre todas tus notas."))
        else:
            popup("Error :(", put_text('¡Calcula algunas notas primero!'))

    language = radio('Choose your Language', type=TEXT,
                     required=True, options=['English', 'Spanish'])

    if language == "English":
        put_markdown(
            "# Grade Calculator\n Welcome to [Miguel Serna's](https://miguelfserna.home.blog/) grade calculator, "
            "this website serves as a simple tool to calculate your grades if your school uses the IB grading system"
            " and you want to get a grade out of 10, for more information click on the"
            " 'How does this work?' button down below, and in order to start calculating click the "
            "'Calculate new subject' button.")
        put_buttons(["Calculate new subject", "How does this work?", "Back to Language select"],
                    onclick=[Eng_Grade_Calculation, Eng_HowDoesItWork, main])
        put_markdown("## Your subjects\n ")
        put_markdown("#### The subjects you calculate will show up here:")
        put_buttons(["Calculate the average"],
                    onclick=[Eng_Global_average])

        while True:
            True

    if language == "Spanish":
        put_markdown("# Calculadora de notas\n Bienvenid@ a la calculadora de notas de [Miguel Serna]"
                     "(https://miguelfserna.home.blog/)"
                     ", esta página web sirve como una herramienta para calcular tus notas si tu colegio utiliza el"
                     " sistema PAI para poner notas y quieres saber cual es tu nota sobre 10, para más información pulsa el "
                     "botón '¿Cómo funciona?' y para calcular tus notas pulsa el botón 'Calcular nueva asignatura'. ")
        put_buttons(["Calcular nueva asignatura", "¿Cómo funciona?", "Volver a elegir idioma"],
                    onclick=[Esp_Grade_Calculation, Esp_HowDoesItWork, main])
        put_markdown("## Tus Asignaturas\n #### Las Asignaturas que calcules saldrán aquí:")
        put_buttons(["Calcular la media"],
                    onclick=[Esp_Global_average])

        while True:
            True


if __name__ == '__main__':
    main()

app = Flask(__name__)

app.add_url_rule("/tool", "webio_view", webio_view(main))

app.run()
