import sys
sys.path.append('{{ GRAPHITE_DIR }}/webapp')

from graphite.wsgi import application
