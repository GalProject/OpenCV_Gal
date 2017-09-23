import cv2 as cv2, os
import argparse

OUTPUT_PATH = 'capture/'
CASCADE_INPUT_PATH = 'haarcasdae_alt.xml'


class VideoCapture:
    # init
    # 0 - the first source video from my computer
    def __init__(self):
        self.count = 0
        self.argsObj = Parse()
        self.faceCascade = cv2.CascadeClassifier(self.argsObj.input_path)
        self.videoSource = cv2.VideoCapture(0)

    def CaptureFrames(self):
        while True:
            # Create a unique number for each frame from the video
            frameNumber = '%08d' % self.count

            # Capture the frame by frame
            ret, frame = self.videoSource.read()

            # set screen color to gray, so the haar cascade can easily detect edges and faces
            screenColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # customize how the cascade detects your face
            faces = self.faceCascade.detectMultiScale(
                screenColor,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            # Display the resulting frame
            cv2.imshow('You!', screenColor)

            # length of faces
            # validate no faces
            if len(faces) == 0:
                #cv2.imshow('live!', frame)
                pass

            # if a face is detected, faces return 1 or more depending on the amount of faces detected

            elif len(faces) > 0:
                print('Face Detected!')

                # Graph the face and drew the rectangle around it (for its because mayb we will have multiple faces)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    #cv2.circle(frame, (x, y), 63, (0, 255, 0), 2)

                #cv2.imwrite(OUTPUT_PATH + frameNumber + '.png', frame)
                #live!
                cv2.imshow('live!', frame)

            # increment count so we get a unique name for each frame
            self.count += 1

            # if 'ESC' is hit -> the video will closed
            if cv2.waitKey(1) == 27:
                break

        # when everything is done->close everything
        self.videoSource.release()
        cv2.waitKey(500)
        cv2.destroyAllWindows()
        cv2.waitKey(500)


def Parse():
    parser = argparse.ArgumentParser(description='Cacade Path for face detection')
    parser.add_argument('-i', '--input_path', type=str, default=CASCADE_INPUT_PATH, help='Cascade input path')
    parser.add_argument('-o', '--output_path', type=str, default=OUTPUT_PATH, help='path for pictures taken')
    args = parser.parse_args()
    return args


def clearImageFolder():
    if not (os.path.exists(OUTPUT_PATH)):
        os.makedirs(OUTPUT_PATH)

    else:
        for files in os.listdir(OUTPUT_PATH):
            filePath = os.path.join(OUTPUT_PATH, files)
            if os.path.isfile(filePath):
                os.unlink(filePath)
            else:
                continue


def main():
    clearImageFolder()

    # Instantiate Class object
    faceDetectImplementation = VideoCapture()

    # Call CaptureFrames from class to begin face detection
    faceDetectImplementation.CaptureFrames()


if __name__ == '__main__':
    main()
