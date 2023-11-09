import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sol", (100, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255))

cv2.putText(img, "Mercurio", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 0, 0))
cv2.putText(img, "Venus", (250, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0))
cv2.putText(img, "Terra", (350, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0))
cv2.putText(img, "Marte", (450, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0))
cv2.putText(img, "Jupiter", (650, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 0, 0))
cv2.putText(img, "Saturno", (780, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0))
cv2.putText(img, "Urano", (950, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0))
cv2.putText(img, "Netuno", (1050, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0))

cv2.imshow("Resultado", img)

cv2.imwrite("Solar_system.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
