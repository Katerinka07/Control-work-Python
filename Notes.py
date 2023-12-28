import json
import os
from datetime import datetime

file_path = 'notes.json'


def load_notes():
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf8') as file:
            notes = json.load(file)
        return notes
    else:
        return []


def save_notes(notes):
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(notes, file, indent=2)


def input_string(promt):
    return input(promt)


def generate_new_id(current_id):
    new_id = 1
    while new_id in current_id:
        new_id += 1
    return new_id


def add_notes():
    heading = input_string('Введите заголовок заметки: ')
    text_notes = input_string('Введит текст заметки: ')
    times = datetime.now().strftime('%d-%m-%y %H:%M:%S')
    note_ids = [note["id"] for note in notes]
    note_id = generate_new_id(note_ids)

    note = {"id": note_id, "heading": heading, "text_notes": text_notes, "times": times}

    if note_id in note_ids:
        note_id = generate_new_id(note_ids)
        note["id"] = note_id

    notes.append(note)
    save_notes(notes)
    print(f'Новая заметка ID {note_id} добавлена')


def viewing():
    for note in notes:
        print(
            f'ID: {note["id"]}; Заголовок: {note["heading"]}; Текст заметки: {note["text_notes"]}; Время создания: {note["times"]}')


def find_note_by_id(note_id):
    return next((note for note in notes if note["id"] == note_id), None)


def change_note():
    note_id = input("Введите номер заметки")
    note = find_note_by_id(note_id)
    if note:
        heading = input('Введите заголовок заметки: ')
        text_notes = input('Введит текст заметки: ')
        note["heading"] = heading
        note["text_notes"] = text_notes
        note["times"] = datetime.now().strftime('%D-%m-%y %H:%M:%S')
        save_notes(notes)
        print('Заметка отедактирована')
    else:
        print('Заметка с указаннм ID не найдена')


def delete_note():
    note_id = input("Введите номер заметки: ")
    note = find_note_by_id(note_id)
    if note:
        notes.remove(note)
        save_notes(notes)
        print('Запись удалена')
    else:
        print('Заметка с указаннм ID не найдена')


def main():
    global notes
    notes = load_notes()
    print('Выберите одно из действий: ',
            '1)Вывести информацию на экран',
            '2)Добавиь заметку',
            '3)Изменить заметку',
            '4)Удалить заметку',
            '5)Выход из программы', sep='\n', end='\n')
    match input('Действие: '):
            case '1':
                viewing()
            case '2':
                add_notes()
            case '3':
                change_note()
            case '4':
                delete_note()
            case '5':
                print('Good bye!')
            case _:
                print('Некорректный ввод')

if __name__ == '__main__':
    main()
