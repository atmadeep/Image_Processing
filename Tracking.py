import cv2
import sys

(major_ver, minor_ver, subminor_ver) = cv2.__version__.split('.')


tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW']
tracker_type = tracker_types[divmod(int(sys.argv[1]),len(tracker_types))[1]]

if int(minor_ver) < 3:
    tracker = cv2.Tracker_create(tracker_type)
else:
    if tracker_type == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    if tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    if tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    if tracker_type == 'TLD':
        tracker = cv2.TrackerTLD_create()
    if tracker_type == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()

video = cv2.VideoCapture(0)
i=0
while(i<10):
    _,frame=video.read()
    i+=1

FOUR_CC = cv2.VideoWriter_fourcc(*"MJPG")
videowriter=cv2.VideoWriter('videos/output_{}.avi'.format(str(tracker_type)),FOUR_CC,20,(640,480))

if not video.isOpened():
    print "Could not open video"
    sys.exit()

bounding_box = cv2.selectROI(frame, False)

ret = tracker.init(frame, bounding_box)
counter=1
while True:

    ret_frame, frame = video.read()
    if not ret_frame:
        break

    timer = cv2.getTickCount()
    ret, bounding_box = tracker.update(frame)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

    if ret:
        p1 = (int(bounding_box[0]), int(bounding_box[1]))
        p2 = (int(bounding_box[0] + bounding_box[2]), int(bounding_box[1] + bounding_box[3]))
        cv2.rectangle(frame, p1, p2, (255, 255, 255), 2, 1)

    else:
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255),
                        2)

    cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2);

    cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2);

    cv2.imshow("Tracking", frame)
    videowriter.write(frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if(k==32):
        cv2.imwrite('other_images/track_{}_{}.jpeg'.format(tracker_type,counter),frame)
        counter+=1
video.release()
cv2.destroyAllWindows()