from django.shortcuts import render 

def question_view(request, i):
    paste_title = 'questao_%s' % i
    ctx = {
        'number': i,
        'text': questions[i]['text'],
        'title': questions[i]['title'],
        'paste_title': paste_title,
    }
    try:
        from pastebin.models import Paste
        paste = Paste.objects.get(title=paste_title)
        ctx['paste_data'] = paste.title
    except:
        ctx['paste_data'] = ('Seu model deve se chamar Paste e você deve fazer '
                             'um paste com o título %r.' % paste_title)
    return render(request, 'static.jinja2', ctx) 

from pastebin.forms import PasteForm
def question_new(request):
    form = PasteForm()
    return render(request, 'forms.html', {'form': form})


questions = {
    3: {
        'title': 'CSS',
        'text': '''
(a) Discuta o que significa a filosofia de desenvolvimento "Mobile First". 
Discuta os aspectos técnicos com relação às implicações no HTML, CSS e 
Javascript. 
    Mobile first trata se da ideologia de pensar no layout da aplicação tomando 
    como base a visibilidade em telas mobiles. As implicações técnicas deste 
    tipo de ideologia de implementação está no fato de ter que pensar em 
    redimensionamento de elementos. Por exemplo o tamanho da fonte utilizada no
    Desktop deve ser maior do que em uma tela mobile. Desta forma, para a 
    implementação de uma funcionalidade do tipo deveria repensar o estilo 
    daquele elemento, ou seja, criar uma outra configuração em css da 
    classe / id do elemento tornando visivel ou não através do media querys.


(b) Nosso site possui um footer responsivo. Ele é mobile first? Justifique.
Caso não seja, explique como consertaríamos o problema.
Não é mobile, pois a implementação do css do footer desktop foi feito primeiro 
pelo fato do media query esta direcionado para quando for no maximo 500px não aparecerá.
Ou seja, foi pensado primeiro o desktop e depois o mobile o que não é o que o mobile first prega.
Basta inverter o css: 
footer {
    display: none;
}

@media only screen and (min-width: 500px) {
    footer {
        background: rgb(21, 207, 198);
        box-shadow: 0 -2px 5px 0 rgba(0, 0, 0, 0.2);
        color: white;
        padding: 30px;
        text-align: center;
    }
}

''',
    },
    
    4: {
        'title': 'Problema N + 1',
        'text': '''
(a) O que é o problema N + 1 que aparece comumente em ORMs? Todos os ORMs estão 
necessariamente sujeitos a este problema ou existem meios de contorná-los? 
O problema N + 1 ocorre quando tem que se em loop fazer consultas no banco utilizando o queryset
, ou seja, ele vai fazer as chamadas de querys de 1 + n(quantidade de interações do loop) vezes.
Enquanto que poderia ser utilizado o select_related que realiza os joins das
tabelas do banco realizando assim somente uma consulta. 

(b) Nosso app não está vulnerável ao problema porque não utiliza de nenhuma 
chave estrangeira. Suponha que o modelo de Paste possua uma referência para 
User. Como o problema apareceria e como poderíamos contorná-lo?
Utilizando o na model que cria a FK o related_name.

''',
    },


    5: {
        'title': 'Converta de Python para Javascript',
        'text': '''

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    is_adult(){
        return this.age >= 18;
    }
    var people = [new Person('Joao', 21), new Person('Maria', 20), new Person('Zé', 8)]
    adults = people.map((x)=>{
        if(x.is_adult()){
            return x;
        }
    });
    var sum = 0;
    people.forEach((x)=>sum+=x.age);
    mean_age = sum / adults.length;
}

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

people = [Person('Joao', 21), Person('Maria', 20), Person('Zé', 8)]
adults = [x for x in people if x.is_adult()]
mean_age = sum(x.age for x in adults) / len(adults)
''',
    },
}