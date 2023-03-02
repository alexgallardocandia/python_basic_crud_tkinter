from tkinter import *
from tkinter import ttk
from countries import *
from tkinter import messagebox
class Ventana(Frame):
    paises = Countries()
#constructor
    def __init__(self, master=None):
        super().__init__(master, width=680, height=260)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenatreview()
        self.enabledbtngc("disabled")
        self.enabledbox("disabled")
        self.id=-1

    def enabledbox(self, estado):
        self.txtISO3.configure(state=estado)
        self.txtCapital.configure(state=estado)
        self.txtCurrency.configure(state=estado)
        self.txtName.configure(state=estado)      
        
    
    def enabledbtn(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
    

    def enabledbtngc(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCacnelar.configure(state=estado)
         

    def clearbox(self):
        self.txtCapital.delete(0, END)
        self.txtISO3.delete(0, END)
        self.txtCurrency.delete(0,END)
        self.txtName.delete(0,END)

    def deleteitem(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def llenatreview(self):
        datos= self.paises.consulta_paises()
        for row in datos:
            self.grid.insert("",END, text=row[0], values=(row[1],row[2],row[3],row[4]))

    def fNuevo(self):
        self.enabledbox("normal")
        self.enabledbtn("disabled")
        self.enabledbtngc("normal")
        self.clearbox()
        self.txtISO3.focus()
    
    def fModificar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')
        if clave == '':
           messagebox.showwarning("Modificar",'Debes seleccionar un elemento.')
        else:
            self.id= clave
            self.enabledbox("normal")
            valores = self.grid.item(selected, 'values')
            self.clearbox()
            self.txtISO3.insert(0, valores[0])
            self.txtName.insert(0, valores[1])
            self.txtCapital.insert(0, valores[2])
            self.txtCurrency.insert(0, valores[3])
        #habilitar y deshabilitar botones.
            self.enabledbtngc("normal")
            self.enabledbtn("disabled")
        #Mandar foco a la primer caja de texto
            self.txtISO3.focus()        
        
    def fEliminar(self):
    #Tomamos el elemento seleccionado y colocamos en la variable selected
        selected = self.grid.focus()
    #separamos la clave del elemento seleccionado y lo guardamos en la variable clave
    #Lo separamos con el "text"
        clave = self.grid.item(selected, "text")
    #condicional para validar que un elemento este seleccionado.    
        if clave == "":
            #Utilizamos messagebox para mandar un mensaje por ventana
            messagebox.showwarning("Eliminar", 'Debe seleccionar un elemento')
        else:
            #cargamos los valores en la variable valores.
            valores = self.grid.item(selected, 'values')
            #Almacenamos algunos valores para mostrar al usuario al momento de confirmar su elminación, almacenamos en la variable data
            data=str(clave)+", "+ valores[0]+", "+valores[1]
            #Consultamos al usuario medio de askquestion si realmente desa elminar el registro seleeccionado.
            #Almacenamos en la variable resp
            resp = messagebox.askquestion("Eliminar",'Deseas elminar el registro seleeccionado?\n'+data)      
            #Validamos la con la variable resp la decision del usuario "si" o "no"
            if resp==messagebox.YES:
                n = self.paises.elimina_pais(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente')
                    self.deleteitem()
                    self.llenatreview()
                else:
                    messagebox.showwarning("Eliminar", 'No se pudo elminar elemento')
               
    def fGuardar(self):
        if self.id==-1:
            self.paises.inserta_pais(self.txtISO3.get(), self.txtName.get(), self.txtCapital.get(),self.txtCurrency.get())
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente')
            
        else:
            self.paises.modifica_pais(self.id, self.txtISO3.get(), self.txtName.get(), self.txtCapital.get(),self.txtCurrency.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente')
            self.id==-1
        self.deleteitem()
        self.llenatreview()
        self.clearbox()
        self.enabledbox("disabled")
        self.enabledbtn("normal")
        self.enabledbtngc("disabled")

    def fCancelar(self):
        q=messagebox.askquestion("Cancelar",'Realmente desea cancelar?')
        if q == messagebox.YES:
            self.clearbox()
            self.enabledbox("disabled")
            self.enabledbtn("normal")
            self.enabledbtngc("disabled")
        
       
    def create_widgets(self):
#Creacion de un frame para asignar los botones
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0, width= 93, height=259)

        self.btnNuevo=Button(frame1, text="Nuevo", command=self.fNuevo, bg="blue", fg="white" )
        self.btnNuevo.place(x=5, y=50, width=80, height=30)

        self.btnModificar=Button(frame1, text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5, y=90, width=80,height=30)

        self.btnEliminar=Button(frame1, text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5, y=130, width=80, height=30)

#Creacion de un nuevo espacio en ventana(frame)
        frame2 = Frame(self,bg="#A0A1A6")
        frame2.place(x=95, y=0, width=150, height=259)
        
#Titulos y inputs
        lbl1 = Label(frame2, text="ISO3:")
        lbl1.place(x=3, y=5)
        self.txtISO3 = Entry(frame2)
        self.txtISO3.place(x=3, y=25, width=50,height=20)

        lbl2 =Label(frame2, text="Country Name: ")
        lbl2.place(x=3, y=55)
        self.txtName=Entry(frame2)
        self.txtName.place(x=3, y=75, width=100, height=20)

        lbl3=Label(frame2, text="Capital: ")
        lbl3.place(x=3, y=105)
        self.txtCapital=Entry(frame2)
        self.txtCapital.place(x=3, y=125, width=100, height=20)

        lbl4=Label(frame2, text="Country Code:")
        lbl4.place(x=3, y=155)
        self.txtCurrency=Entry(frame2)
        self.txtCurrency.place(x=3, y=175, width=50, height=20)

#Botones de Guardar y Cancelar
        self.btnGuardar=Button(frame2, text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=3, y=210, width=70, height=20)

        self.btnCacnelar=Button(frame2, text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCacnelar.place(x=80, y=210, width=70, height=20)
#Creacion de nuevo frame para barra de scroll
        frame3 = Frame(self,bg="yellow")
        frame3.place(x=247, y= 0, width=420, height=259)
#Creacion de grilla
        self.grid = ttk.Treeview(frame3, columns=("col1", "col2", "col3", "col4"))      

        self.grid.column("#0", width=60)
        self.grid.column("col1", width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)

        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="ISO3", anchor=CENTER)
        self.grid.heading("col2", text="Country Name", anchor=CENTER)
        self.grid.heading("col3", text="Capital", anchor=CENTER)
        self.grid.heading("col4", text="Country Code", anchor=CENTER)

#colocacion del scrollbar
        self.grid.pack(side=LEFT, fill=Y)

        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill= Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
#no permitir que se pueda seleccionar mas de un item
        self.grid['selectmode']='browse'        