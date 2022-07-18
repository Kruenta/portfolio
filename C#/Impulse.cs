using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// ������ ��� ������������. (����������)
public class Impulse : MonoBehaviour
{
 
    public float thrust = 1.0f; // ���� ������ 
    public Rigidbody rb;
    void OnCollisionEnter(Collision otherRB)
    {
        if (otherRB.gameObject.tag == "Box")
        {
            rb = GetComponent<Rigidbody>();
            rb.AddForce(0, thrust, 0, ForceMode.Impulse);
        }
    }
}
