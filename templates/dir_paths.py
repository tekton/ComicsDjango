{% load text_tags %}
<div>
    <table>
	{% for file in recentFiles %}
		<tr>		    
		    <td>{{file.dir_path__count}}</td><td><a href="{% url HomeComics.views.view_dir_path %}?dir_path={{file.dir_path|hexVert}}">{{file.dir_path}}</td>
		</tr>
	{% endfor %}
	</table>
</div>