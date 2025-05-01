#!/bin/bash
set -e

GREEN="\033[0;32m"
RED="\033[0;31m"
RESET="\033[0m"

echo -e "${GREEN}1. Остановка предыдущих контейнеров...${RESET}"
sudo docker-compose down || echo -e "${RED}Контейнеры уже остановлены.${RESET}"

echo -e "${GREEN}2. Удаление старых томов...${RESET}"
sudo docker volume prune -f || echo -e "${RED}Не удалось очистить тома.${RESET}"

echo -e "${GREEN}3. Запуск контейнеров...${RESET}"
sudo docker-compose up --build || { echo -e "${RED}Ошибка запуска контейнеров!${RESET}"; exit 1; }

echo -e "${GREEN}Проект успешно запущен!${RESET}"