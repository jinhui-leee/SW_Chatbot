from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoticeForm, QATableForm
from .models import Notice, QATable
# Create your views here.

# 비밀번호 페이지
def admin_page(request):
    if request.method == "POST":
        password = request.POST.get('password')
        if password == '1234':  # 관리자 비밀번호
            # 비밀번호가 일치하면 메인 페이지로 리디렉션
            return redirect('management')
        else:
            # 비밀번호가 틀렸을 때 별도의 응답 없이 아무 것도 하지 않음
            return render(request, 'chatbotAdmin/admin_page.html')

    return render(request, 'chatbotAdmin/admin_page.html')

# 비밀번호 해제 후, 메인 화면
def management(request):
    return render(request, 'chatbotAdmin/management.html')

# 공지 추가 페이지
def add_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            # created_at은 자동으로 현재 시간으로 설정됩니다.
            notice.save()
            return redirect('add_notice')
        else:
            print(form.errors)
        form = NoticeForm()
    return render(request, 'chatbotAdmin/add_notice.html')

# 질문 답변 페이지
def add_question_answer(request):
    if request.method == "POST":
        form = QATableForm(request.POST)
        if form.is_valid():
            # 폼에서 데이터 가져오기
            instance = form.save(commit=False)

            # answer_status 값을 'Y'로 설정
            instance.question_content.answer_status = 'Y'
            instance.question_content.save()

            instance.save()

            return redirect('add_question_answer')  # 저장 후 폼 초기화
    else:
        form = QATableForm()

    return render(request, 'chatbotAdmin/add_question_answer.html', {'form': form})

# DB 관리 페이지
def chatbot_db_management(request):
    if request.method == "POST":
        db_type = request.POST.get('db_type')
        if db_type == '공지':
            notices = Notice.objects.order_by('-created_at')
            return render(request, 'chatbotAdmin/chatbot_db_management.html', {'notices': notices})
        elif db_type == '질문 답변':
            qatables = QATable.objects.order_by('-created_at')
            return render(request, 'chatbotAdmin/chatbot_db_management.html', {'qatables': qatables})

    return render(request, 'chatbotAdmin/chatbot_db_management.html')

# DB 관리 페이지 공지 상세 보기
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'chatbotAdmin/notice_detail.html', {'notice': notice})

# DB 관리 페이지 공지 상세 보기
def qatalbe_detail(request, pk):
    qatable = get_object_or_404(QATable, pk=pk)
    return render(request, 'chatbotAdmin/qatable_detail.html', {'qatable': qatable})