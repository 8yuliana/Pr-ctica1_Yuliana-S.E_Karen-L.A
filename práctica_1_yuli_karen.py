# -*- coding: utf-8 -*-
"""Práctica 1_Yuli_Karen.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12JrkAhMTs0989PWWdA72CMN63zcHrkqz
"""

#PRÁCTICA "VALIDACIÓN DE PARÉNTESIS" DE YULIANA SÁNCHEZ ESCOBAR Y KAREN LAZO ALARCÓN

def cadena_de_parentesis_bien_formados(cadena):
        """
        Esta función sirve para evaluar la validación de paréntesis bien formados en una cadena.
        La evaluación consisitirá en cadenas que contengan únicamente caracteres '(' y ')'.

        Usé los returns como: Booleno = True si la cadena de paréntesis está bien formada, Booleano = False de lo contrario.
        """
        pila = [] #Se usa la estructura de datos pila porque ayudará a apilar cada paréntesis que se ingrese
        for i in cadena:
            if i == '(':
                pila.append(i) #Agrega elementos a la lista/pila
            elif i == ')': # Si la pila está vacía o el último elemento no es un '(', la cadena no está bien formada.
                if not pila or pila[-1] != '(': # pila[-1] se refiere al último elemento de la lista. El operador != significa distinto a
                    print("La cadena NO está bien formada. El paréntesis de cierre ')' no tiene su correspondiente '('.")
                    return False
                else:
                    pila.pop() #Si el elemento siguiente sí corresponde al alfabeto pop lo que hace es tomar ese elemento y emparejarlo con el.
            else:
                print(f"La cadena NO está bien formada: El caracter '{i}' no pertenece al alfabeto de paréntesis.") # Si el caracter no es '(' ni ')', la cadena no es válida.
                return False                                                                                        # La f permite que python identifique el caracter que es ajeno al alfabeto.

        # Si la pila está vacía al final, significa que todos los paréntesis tienen sus correspondientes cerraduras y la cadena está bien formada.

        if not pila: #Evalua que la pila esté vacía, es decir, todos los paréntesis están bien formados y por eso devuelve True.
            print("La cadena está bien formada")
            return True
        else: #Si la pila NO está vacía los paréntesis no están bien formados, por eso devolverá False.
            print("La cadena NO está bien formada: La cadena tiene paréntesis de apertura '(' sin su correspondiente cierre ')'.")
            return False

if __name__ == "__main__":
    cadena = input("Ingrese una cadena de paréntesis: ")
    resultado = cadena_de_parentesis_bien_formados(cadena)
    print("Resultado:", resultado)