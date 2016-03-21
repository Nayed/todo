'use strict'

let todoApp = angular.module('todoApp', [
    'todoList'
])

let todoList = angular.module('todoList', [])

todoList.controller('todoCtrl', ['$scope', $scope => {
        let todos = $scope.todos = []

        // Add todo
        $scope.addTodo = () => {
            let newTodo = $scope.newTodo.trim()
            if (!newTodo.length) {
                return
            }
            todos.push({
                title: newTodo,
                completed: false
            })

            $scope.newTodo = ''
        }

        // Remove todo
        $scope.removeTodo = todo => {
            todos.splice(todos.indexOf(todo), 1)
        }

        // Mark - unmark all todos
        $scope.markAll = completed => {
            todos.forEach(todo => {
                todo.completed = !completed
            })
        }

        // Delete todos marked
        $scope.clearCompletedTodos = () => {
            $scope.todos = todos = todos.filter(todo => {
                return !todo.completed
            })
        }
    }
])

