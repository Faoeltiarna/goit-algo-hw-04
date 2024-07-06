def total_salary(path: str) -> tuple:
# для прикладу вставив дві строчки коду для створення файлу з переліком працівників і заробітньої плати
    with open('test_file.txt', 'w') as fh:
        fh.write('Alex Korp,3000\nNikita Borisenko,4000\nSitarama Raju,1000\nPeter Jane,2575')
    try:
        with open(path, 'r') as fh:
            lst = [el.strip() for el in fh.readlines()]
            elem_lst = [el.split(',') for el in lst]
            total = 0
            for item in elem_lst:
                total += int(item[1])
            average = total / len(elem_lst)
    except FileNotFoundError:
        print("Your file is not found")
    except ValueError:
        print("Your file has errors")

    return total, average


try:
    total, average = total_salary('test_file.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except Exception as e:
    print(f"An error occurred: {e}")
