#!/usr/bin/bash

function gitcd() {
  builtin cd "$@" && pwd
}
