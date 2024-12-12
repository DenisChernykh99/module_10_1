import time
import threading


def write_words(word_count, file_name):

    with open(file_name, 'a', encoding='utf-8') as f:
        for number in range(word_count):
            f.write(f'Какое-то слово № {number+1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')



start_time1 = time.perf_counter()

write1 = write_words(10, 'example1.txt')
write2 = write_words(30, 'example2.txt')
write3 = write_words(200, 'example3.txt')
write4 = write_words(100, 'example4.txt')

end_time = time.perf_counter()
total_time = end_time - start_time1
print(f'Общее время выполнения: {total_time:.2f} секунд')

start_time2 = time.perf_counter()

thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time2 = time.perf_counter()
total_time = end_time2 - start_time2
print(f'Общее время выполнения: {total_time:.2f} секунд')