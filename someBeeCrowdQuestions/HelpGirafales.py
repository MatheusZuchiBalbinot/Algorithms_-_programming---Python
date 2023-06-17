# Minutos antes do término das aulas, professor Girafales passa uma lista de presença. Certo dia, ele resolveu conferir as assinaturas e notou que alguns alunos assinavam diferente em algumas aulas e desconfiou que alguém poderia estar assinando por eles. Como o professor possui muitos alunos e pouco tempo (o café com dona Florinda é prioridade), ele pediu sua ajuda para validar as assinaturas. Uma assinatura é considerada falsa se houver mais de uma diferença entre a original e a que estiver sendo checada. Considere diferença uma troca de maiúscula para minúscula ou o contrário. Entrada Haverá diversos casos de testes. A primeira linha de cada caso inicia com um inteiros N (1 ≤ N ≤ 50) representando a quantidade de alunos de sua turma. As próximas N linhas serão da seguinte forma: Nome do aluno   Assinatura Original A seguir haverá um inteiro M (0 ≤ M ≤ N), representando a quantidade de alunos que compareceram a uma aula. M linhas seguem, no seguinte formato: Nome do aluno   Assinatura na aula Todos os alunos possuem apenas o primeiro nome na lista, nenhum nome se repete e todos os nomes contêm no máximo 20 letras (a-z A-Z). A entrada termina com N = 0, a qual não deve ser processada. Saída Para cada caso, exiba uma única linha, a quantidade de assinaturas falsas encontradas.

while True:
    n = int(input())
    fake_signatures = 0
    if n == 0:
        break
    original_signature = []
    for i in range(n):
        name, t1_signature = list(map(str,input("").split()))
        original_signature.append(t1_signature)

    m = int(input())

    for i in range(m): 
        name_v2, signature = input("").split()
        string_one = list(signature)
        for j in original_signature:
            if signature.lower() == j.lower():
                string_two = list(j)
        errors = 0
        for k in range(len(string_one)):
            if string_two[k] != string_one[k]:
                errors += 1
        if errors > 1:
            fake_signatures += 1
    print(fake_signatures)