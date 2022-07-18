using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// Скрипт для платформ (доработать)
public class updown : MonoBehaviour
{
    float speed = 2f; //Скорость перемещения платформы
    float height = 2f; // Высота перемещения платформы
    float startY = 0f; // Откуда начинает (вроде)
 
    void Update()
    {

        var newY = startY + height * Mathf.Sin(Time.time * speed);
        transform.position = new Vector3(transform.position.x, newY, transform.position.z);
    }
}
