# PROJECT_NAME defaults to name of the current directory.
# # should not to be changed if you follow GitOps operating procedures.
#
build:
	docker build -t todolist .

clean: 
	docker image rm todolist
	docker image prune -a

prune: 
	docker system prune -a



