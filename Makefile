git:
	git add .
	git commit -m "Update"
	git push

site:
	python3 -m http.server 8000 --directory . --bind 127.0.0.1
