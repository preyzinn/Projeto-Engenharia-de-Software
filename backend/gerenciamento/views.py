from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        return redirect('gerenciamento:selecao_empresa')
    return render(request, 'gerenciamento/login.html')

def selecao_empresa(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'create':
            # cria e vai para a dashboard (mock)
            return redirect('gerenciamento:dashboard')
        elif action == 'enter':
            company_id = request.POST.get('company_id')
            if company_id:
                # entra e vai para a dashboard (mock)
                return redirect('gerenciamento:dashboard')
    return render(request, 'gerenciamento/company_selection.html')

# Mock storage in memory
PROJECTS = [
    {'id': 1, 'name': 'Sistema Financeiro', 'access': 'member', 'admin': 'usuarioX'},
    {'id': 2, 'name': 'App Mobile', 'access': 'none', 'requested': False, 'admin': 'usuarioY'},
]

REQUESTS = []

def dashboard(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        project_name = request.POST.get('project_name')
        project_id = request.POST.get('project_id')
        
        if action == 'create_project' and project_name:
            new_id = len(PROJECTS) + 1
            PROJECTS.append({
                'id': new_id, 
                'name': project_name, 
                'access': 'admin', 
                'admin': 'você'
            })
        elif action == 'request_access':
            for p in PROJECTS:
                if str(p['id']) == str(project_id):
                    p['requested'] = True
                    # Adiciona a solicitacao no mockup array
                    REQUESTS.append({'project_id': p['id'], 'project_name': p['name'], 'user': 'Você'})
                    break

    return render(request, 'gerenciamento/dashboard.html', {'projects': PROJECTS})

def project_detail(request, project_id):
    # Procura projeto
    project = next((p for p in PROJECTS if str(p['id']) == str(project_id)), None)
    
    # Simula aprovacao de acesso: se o projeto for seu (access == admin), voce pode aprovar os requests
    my_requests = [r for r in REQUESTS if str(r['project_id']) == str(project_id)]

    if request.method == 'POST':
        action = request.POST.get('action')
        req_user = request.POST.get('req_user')
        if action == 'approve':
            # aprova request
            pass

    return render(request, 'gerenciamento/project_detail.html', {'project': project, 'requests': my_requests})
