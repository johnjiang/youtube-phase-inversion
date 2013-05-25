from __future__ import unicode_literals
from flask import Response
import sh

from app import app


@app.route("/youtube/<string:key>.mp3")
def youtube_audio_invert(key):
    filename = key + ".flv"
    mp3 = key + ".mp3"
    inverted_filename = key + "_inverted.mp3"

    youtube_dl = sh.Command("/usr/local/share/python/youtube-dl")
    sox = sh.Command("/usr/local/bin/sox")
    ffmpeg = sh.Command("/usr/local/bin/ffmpeg")

    # download the youtube flv file
    youtube_output = youtube_dl("http://www.youtube.com/watch?v={key}".format(key=key), "--id")
    app.logger.info(youtube_output)

    # extract audio from flv file
    ffmpeg_output = ffmpeg("-i", filename, "-acodec", "libmp3lame", "-aq", "4", mp3, "-y")
    app.logger.info(ffmpeg_output)

    # invert one channel of the audio
    sox_output = sox(mp3, inverted_filename, "remix", "1,2i")
    app.logger.info(sox_output)

    return Response(open(inverted_filename, "rb"), content_type="audio/mpeg")
