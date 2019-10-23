import struct


class VideoStream:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename, 'rb')
            print '-'*60 + "\nVideo file : |" + filename + "| read\n" + '-'*60
        except:
            print "read " + filename + " error"
            raise IOError
        self.frameNum = 0

    def nextFrame(self):
        """Get next frame."""

        data = self.file.read(5)
        data = bytearray(data)

        data_int = (data[0] - 48) * 10000 + (data[1] - 48) * 1000 + (data[2] - 48) * \
            100 + (data[3] - 48) * 10 + (data[4] -
                                         48)

        final_data_int = data_int

        if data:

            framelength = final_data_int
            frame = self.file.read(framelength)
            if len(frame) != framelength:
                raise ValueError('incomplete frame data')

            self.frameNum += 1
            print '-'*10 + "\nNext Frame (#" + str(self.frameNum) + ") length:" + str(framelength) + "\n" + '-'*10

            return frame

    def frameNbr(self):
        """Get frame number."""
        return self.frameNum
