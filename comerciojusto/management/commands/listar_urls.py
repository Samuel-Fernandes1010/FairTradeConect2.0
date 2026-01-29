from django.core.management.base import BaseCommand
from django.urls import get_resolver

class Command(BaseCommand):
    help = 'Lista todas as URLs do projeto'

    def handle(self, *args, **options):
        resolver = get_resolver()
        
        def get_urls(url_patterns, prefix=''):
            urls = []
            for pattern in url_patterns:
                if hasattr(pattern, 'url_patterns'):
                    urls += get_urls(pattern.url_patterns, prefix + str(pattern.pattern))
                else:
                    url = prefix + str(pattern.pattern)
                    name = getattr(pattern, 'name', None)
                    urls.append((name, url))
            return urls
        
        all_urls = get_urls(resolver.url_patterns)
        
        self.stdout.write("\n=== URLs relacionadas a pagamento ===\n")
        for name, url in all_urls:
            if name and ('checkout' in name.lower() or 'pagamento' in name.lower() or 'sucesso' in name.lower()):
                self.stdout.write(f"{name:30} -> {url}")
