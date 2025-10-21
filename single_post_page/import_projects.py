from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = 'Imports GitHub projects as blog posts'

    def handle(self, *args, **kwargs):
        # 잭(Jack)님의 GitHub 공개 레포지토리를 기반으로 프로젝트 목록을 정의합니다.
        projects = [
            {
                'title': '개인 블로그 개발 프로젝트 (back12)',
                'hook_text': 'Django와 Tailwind CSS를 이용한 나만의 기술 블로그 만들기',
                'content': """
현재 개발 중인 바로 이 블로그 프로젝트입니다.

Django의 강력한 백엔드 기능과 Tailwind CSS의 유연한 스타일링을 결합하여, 저만의 아이덴티티가 담긴 기술 블로그를 만들고 있습니다. 

주요 특징:
- Django 클래스 기반 뷰(CBV)를 활용한 효율적인 개발
- Tailwind CSS를 이용한 모던하고 반응형적인 UI/UX
- 관리자 페이지에서 프로필 및 게시물 관리 기능
- Django 템플릿 상속을 통한 코드 재사용성 극대화

이 프로젝트를 통해 Django 심화 개념과 프론트엔드 기술의 결합을 깊이 있게 학습하고 있습니다.
""",
                'github_url': 'https://github.com/jackdiary/back12'
            },
            {
                'title': 'Do It! Django 2.0 실습 프로젝트',
                'hook_text': 'Django 2.0 버전으로 블로그의 기본기를 다진 프로젝트',
                'content': """
'Do It! Django A to Z' 책의 2.0 버전을 따라가며 진행한 블로그 프로젝트입니다. 

이 프로젝트를 통해 Django의 기본적인 MTV(Model-Template-View) 패턴, URL 라우팅, 템플릿 시스템 등 핵심 개념을 익혔습니다. Bootstrap을 사용하여 기본적인 프론트엔드 디자인을 적용하는 방법도 함께 학습했습니다.
""",
                'github_url': 'https://github.com/jackdiary/do-it-django-prj-2.0'
            },
            # 여기에 새로운 프로젝트를 계속 추가할 수 있습니다.
            # {
            #     'title': '새로운 프로젝트 이름',
            #     'hook_text': '프로젝트에 대한 한 줄 요약',
            #     'content': '프로젝트에 대한 상세한 설명...',
            #     'github_url': 'https://github.com/jackdiary/repository-name'
            # },
        ]

        for project in projects:
            # 동일한 제목의 포스트가 이미 존재하면 생성하지 않고, 없으면 새로 생성합니다.
            post, created = Post.objects.get_or_create(
                title=project['title'],
                defaults={
                    'hook_text': project['hook_text'],
                    'content': project['content'] + f"\n\n[GitHub에서 프로젝트 보기]({project['github_url']})",
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created post: "{post.title}"'))
            else:
                self.stdout.write(self.style.WARNING(f'Post "{post.title}" already exists. Skipped.'))

        self.stdout.write(self.style.SUCCESS('Finished importing projects.'))