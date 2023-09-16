from django.shortcuts import render

# Create your views here.

# def contact(request):
#     return render(request,'./first_app/index.html', {'courses' : [
#         {
#             'id': 1,
#             'course' : 'C',
#             'teacher' : 'Rahim'
#         },
#         {
#             'id': 2,
#             'course' : 'C++',
#             'teacher' : 'Kahim'
#         },
#         {
#             'id': 3,
#             'course' : 'Python',
#             'teacher' : 'Fahim'
#         }
#     ]})

def contact(request):
    return render(request,'./first_app/index.html', {"name" : "I am Rahim",
    "marks" :86, "list" : [24,3,10,5], "blog" : "Lorem ipsum dolor, sit amet consectetur adipisiciting elit. Harum quae temora fugit laborum voluptas mollitia. Exlicabo earum assumenda obcaecati et."})



# context={'author ':'phitron','age ':19,'marks ':89}