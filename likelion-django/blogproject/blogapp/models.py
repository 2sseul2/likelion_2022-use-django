from django.db import models

class Blog(models.Model):
    # primary key를 자동으로 지정해준다. id, 1 부터 시작.
    title = models.CharField(max_length=200)
    body = models.TextField()
    # 사진이 업로드되면, media/blog_photo 자동 생성하여 파일 저장하겠다.
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)

    # 객체의 이름을 title로 반환하여 지정해줌.
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시글의 댓글인지, Blog 모델을 참조해야함.
    # 같이 삭제된다. on_delete=models.CASCADE
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
