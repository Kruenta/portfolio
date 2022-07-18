using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 // Основной скрипт на перемещение 
public class Playertest : MonoBehaviour
{
    public GameObject MainCamera; //аттач главной камеры для получения вектора направления движения
    public GameObject Player; //Объект игрок

    public static bool _gameover; //условие проигрыша

    private float speed; //Скорость перемещения
    private Rigidbody rb; //Физическое тело
    private bool grounded; // На земле ли персонаж
    private bool moveForward; // Двигается вперед персонаж
    private bool moveBack; // Двигается назад персонаж
    private bool moveRight; // Двигается право персонаж
    private bool moveLeft; // Двигается влево персонаж
    public float JumpForce = 200;  // Сила прыжка
    private bool isGrounded;       //Проверка наличия тега земли
    public AudioSource audio;    // Аудио

    // Проверка наличие земли и прекращения аудио сопровождения.
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

    //Задаем переменные при старте игры
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

    //Теперь опишем, что должен делать персонаж при нажатых клавишах

    void Update()
    {
        //Двигаемся вперед по вектору камеры
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
        //Движение назад по вектору камеры
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

        //Движение вправо по вектору камеры
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
        //Движение влево по вектору камеры
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

            if (Input.GetKeyDown(KeyCode.LeftControl))    // Остановка
        {
            rb.velocity = new Vector3(0, 0, 0);
            rb.angularVelocity = new Vector3(0, 0, 0);
        }
            if (Input.GetKeyDown(KeyCode.Space) && isGrounded)  // Прыжок
        {
            audio.Play();
            rb.AddForce(Vector3.up * JumpForce);
        }
    }
}