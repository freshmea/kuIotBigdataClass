#include <stdio.h>
#include <ao/ao.h>
#include <mpg123.h>

#define BITS 8

int main(int argc, char **argv)
{
    mpg123_handle *mh;
    unsigned char *buffer;
    size_t buffer_size;
    size_t done;
    int err;

    int driver;
    ao_device *dev;

    ao_sample_format format;
    int channels, encoding;
    long rate;

    // Initialize libraries
    ao_initialize();
    mpg123_init();
    mh = mpg123_new(NULL, &err);
    mpg123_open(mh, "BGMTetrisBradinsky.mp3");
    mpg123_getformat(mh, &rate, &channels, &encoding);

    // Set the output format
    format.bits = mpg123_encsize(encoding) * BITS;
    format.rate = rate;
    format.channels = channels;
    format.byte_format = AO_FMT_NATIVE;
    format.matrix = 0;
    driver = ao_default_driver_id();

    dev = ao_open_live(driver, &format, NULL);

    // Decode and play
    buffer_size = mpg123_outblock(mh);
    buffer = (unsigned char *)malloc(buffer_size * sizeof(unsigned char));

    while (mpg123_read(mh, buffer, buffer_size, &done) == MPG123_OK)
    {
        ao_play(dev, buffer, done);
    }

    // Clean up
    free(buffer);
    ao_close(dev);
    mpg123_close(mh);
    mpg123_delete(mh);
    mpg123_exit();
    ao_shutdown();

    return 0;
}

/*
#include <stdio.h>
#include <ao/ao.h>
#include <mpg123.h>
#include <pthread.h>

#define BITS 8

int game = 0; // Global variable

void *play_music(void *arg)
{
    mpg123_handle *mh;
    unsigned char *buffer;
    size_t buffer_size;
    size_t done;
    int err;

    int driver;
    ao_device *dev;

    ao_sample_format format;
    int channels, encoding;

    // ... (나머지 코드)

    while (mpg123_read(mh, buffer, buffer_size, &done) == MPG123_OK)
    {
        if (game == 1) // Check the value of 'game'
        {
            break; // Stop playing music
        }
        ao_play(dev, buffer, done);
    }

    // ... (나머지 코드)

    return NULL;
}

int main(int argc, char **argv)
{
    pthread_t thread_id;

    // Create a new thread that will execute 'play_music'
    pthread_create(&thread_id, NULL, &play_music, NULL);

    // ... (다른 작업)

    // Wait for the thread to finish
    pthread_join(thread_id, NULL);

    return 0;
}

*/