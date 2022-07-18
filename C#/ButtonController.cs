using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
// Кнопки. НГ, Рестарт, Загрузки, Рестарта
public class ButtonController : MonoBehaviour
{
    public static ButtonController Instance;
    public Canvas canvas;

    void Start()
    {
        Instance = this;

        canvas.enabled = false;
    }
    public void onClick()
    {
        Debug.Log("клик");

    }

    public void ShowFinish()
    {
        Time.timeScale = 0;
        canvas.enabled = true;
    }

    public void RestartGame()
    {
        Time.timeScale = 1;
        PlayerController.Points = 0;
        SceneManager.LoadScene(0);

    }

    public void LoadNextLevel(int index)
    {
        Time.timeScale = 1;
        SceneManager.LoadScene(index);

    }
}
