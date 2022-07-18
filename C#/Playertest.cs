using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 // �������� ������ �� ����������� 
public class Playertest : MonoBehaviour
{
    public GameObject MainCamera; //����� ������� ������ ��� ��������� ������� ����������� ��������
    public GameObject Player; //������ �����

    public static bool _gameover; //������� ���������

    private float speed; //�������� �����������
    private Rigidbody rb; //���������� ����
    private bool grounded; // �� ����� �� ��������
    private bool moveForward; // ��������� ������ ��������
    private bool moveBack; // ��������� ����� ��������
    private bool moveRight; // ��������� ����� ��������
    private bool moveLeft; // ��������� ����� ��������
    public float JumpForce = 200;  // ���� ������
    private bool isGrounded;       //�������� ������� ���� �����
    public AudioSource audio;    // �����

    // �������� ������� ����� � ����������� ����� �������������.
    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.tag == "Ground")
        {
            audio.Stop();

        }
    }
    private void OnCollisionStay(Collision collision)
    {
        if (collision.gameObject.tag == "Ground")
        {

            isGrounded = true;
        }
    }

    private void OnCollisionExit(Collision collision)
    {
        if (collision.gameObject.tag == "Ground")
        {
            isGrounded = false;
        }
    }

    //������ ���������� ��� ������ ����
    void Start()
    {
        grounded = true;
        rb = Player.GetComponent<Rigidbody>();
        _gameover = false;
        speed = 300;
        moveForward = false;
        moveBack = false;
        moveRight = false;
        moveLeft = false;
    }

    //������ ������, ��� ������ ������ �������� ��� ������� ��������

    void Update()
    {
        //��������� ������ �� ������� ������
        if (Input.GetKey(KeyCode.W) & _gameover == false)
        {
            moveForward = true;
            if (grounded == true)
            {
                rb.AddForce(MainCamera.transform.forward * speed * Time.deltaTime);
            }
            else
            {
                rb.AddForce(0f, 0f, 0f);
            }
        }
        else
        {
            moveForward = false;
        }
        //�������� ����� �� ������� ������
        if (Input.GetKey(KeyCode.S) & _gameover == false)
        {
            if (grounded == true)
            {
                rb.AddForce(-MainCamera.transform.forward * speed * Time.deltaTime);
                moveBack = true;
            }
            else
            {
                rb.AddForce(0f, 0f, 0f);
            }
        }
        else
        {
            moveBack = false;
        }

        //�������� ������ �� ������� ������
        if (Input.GetKey(KeyCode.D) & _gameover == false)
        {
            if (grounded == true)
            {
                rb.AddForce(MainCamera.transform.right * speed * Time.deltaTime);
                moveRight = true;
            }
            else
            {
                rb.AddForce(0f, 0f, 0f);
            }
        }
        else
        {
            moveRight = false;
        }
        //�������� ����� �� ������� ������
        if (Input.GetKey(KeyCode.A) & _gameover == false)
        {
            if (grounded == true)
            {
                rb.AddForce(-MainCamera.transform.right * speed * Time.deltaTime);
                moveLeft = true;
            }
            else
            {
                rb.AddForce(0f, 0f, 0f);
            }
        }
        else
        {
            moveLeft = false;
        }

            if (Input.GetKeyDown(KeyCode.LeftControl))    // ���������
        {
            rb.velocity = new Vector3(0, 0, 0);
            rb.angularVelocity = new Vector3(0, 0, 0);
        }
            if (Input.GetKeyDown(KeyCode.Space) && isGrounded)  // ������
        {
            audio.Play();
            rb.AddForce(Vector3.up * JumpForce);
        }
    }
}