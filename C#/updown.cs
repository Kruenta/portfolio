using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// ������ ��� �������� (����������)
public class updown : MonoBehaviour
{
    float speed = 2f; //�������� ����������� ���������
    float height = 2f; // ������ ����������� ���������
    float startY = 0f; // ������ �������� (�����)
 
    void Update()
    {

        var newY = startY + height * Mathf.Sin(Time.time * speed);
        transform.position = new Vector3(transform.position.x, newY, transform.position.z);
    }
}
